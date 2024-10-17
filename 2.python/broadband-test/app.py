import time
import subprocess
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import queue
import csv
import os
from datetime import datetime
import statistics
import shutil

# Configuration
PING_INTERVAL = 1  # seconds
PING_TIMEOUT = 5  # seconds
HISTORY_LENGTH = 3600  # 1 hour of data
HOSTS = ['1.1.1.1', 'amazon.com', 'cloudflare.com']  # List of hosts to ping
GRAPH_UPDATE_INTERVAL = 5000  # milliseconds
DNS_TEST_INTERVAL = 60  # seconds
TRACEROUTE_INTERVAL = 300  # seconds
OUTPUT_DIR = 'network_diagnostics'

# Check if traceroute is installed
TRACEROUTE_AVAILABLE = shutil.which('traceroute') is not None

if not TRACEROUTE_AVAILABLE:
    print("Warning: 'traceroute' command not found. Traceroute functionality will be disabled.")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Data storage
ping_data = {host: queue.Queue(maxsize=HISTORY_LENGTH) for host in HOSTS}
summary_data = {host: {'min': float('inf'), 'max': 0, 'avg': 0, 'loss': 0} for host in HOSTS}
dns_data = {host: '' for host in HOSTS}
traceroute_data = {host: '' for host in HOSTS}
ping_thread_stop = threading.Event()

def ping_host(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', '-W', str(PING_TIMEOUT), host], universal_newlines=True)
        latency = float(output.split('time=')[1].split(' ms')[0])
    except subprocess.CalledProcessError:
        latency = None
    except IndexError:
        latency = None
    return latency

def dns_resolution_test(host):
    try:
        output = subprocess.check_output(['dig', '+short', host], universal_newlines=True)
        return output.strip()
    except subprocess.CalledProcessError:
        return "Failed"

def traceroute_test(host):
    if not TRACEROUTE_AVAILABLE:
        return "Traceroute not available"
    try:
        output = subprocess.check_output(['traceroute', '-w', '2', '-q', '1', '-m', '15', host], universal_newlines=True)
        return output
    except subprocess.CalledProcessError:
        return "Failed"

def update_summary(host, latency):
    if latency is not None:
        summary_data[host]['min'] = min(summary_data[host]['min'], latency)
        summary_data[host]['max'] = max(summary_data[host]['max'], latency)
        
        # Update average
        queue_data = list(ping_data[host].queue)
        valid_latencies = [lat for _, lat in queue_data if lat is not None]
        summary_data[host]['avg'] = statistics.mean(valid_latencies) if valid_latencies else 0
        
        # Update packet loss
        total_pings = len(queue_data)
        lost_pings = sum(1 for _, lat in queue_data if lat is None)
        summary_data[host]['loss'] = (lost_pings / total_pings) * 100 if total_pings > 0 else 0

def ping_thread():
    last_dns_test = 0
    last_traceroute = 0
    
    with open(os.path.join(OUTPUT_DIR, 'ping_data.csv'), 'w', newline='') as ping_file, \
         open(os.path.join(OUTPUT_DIR, 'dns_tests.log'), 'w') as dns_file, \
         open(os.path.join(OUTPUT_DIR, 'traceroute_tests.log'), 'w') as traceroute_file:
        
        ping_writer = csv.writer(ping_file)
        ping_writer.writerow(['Timestamp'] + HOSTS)
        
        while not ping_thread_stop.is_set():
            current_time = time.time()
            row = [datetime.fromtimestamp(current_time).isoformat()]
            
            for host in HOSTS:
                latency = ping_host(host)
                if ping_data[host].full():
                    ping_data[host].get()
                ping_data[host].put((current_time, latency))
                row.append(str(latency) if latency is not None else "None")
                update_summary(host, latency)
            
            ping_writer.writerow(row)
            ping_file.flush()
            
            if current_time - last_dns_test >= DNS_TEST_INTERVAL:
                dns_file.write(f"\n--- DNS Resolution Test at {datetime.fromtimestamp(current_time).isoformat()} ---\n")
                for host in HOSTS:
                    result = dns_resolution_test(host)
                    dns_data[host] = result
                    dns_file.write(f"{host}: {result}\n")
                dns_file.flush()
                last_dns_test = current_time
            
            if TRACEROUTE_AVAILABLE and current_time - last_traceroute >= TRACEROUTE_INTERVAL:
                traceroute_file.write(f"\n--- Traceroute Test at {datetime.fromtimestamp(current_time).isoformat()} ---\n")
                for host in HOSTS:
                    result = traceroute_test(host)
                    traceroute_data[host] = result.split('\n')[-1] if result != "Failed" else "Failed"
                    traceroute_file.write(f"Traceroute to {host}:\n{result}\n")
                traceroute_file.flush()
                last_traceroute = current_time
            
            time.sleep(PING_INTERVAL)

def update_plot(frame):
    for i, host in enumerate(HOSTS):
        data = list(ping_data[host].queue)
        times, latencies = zip(*data)
        times = [(t - times[0]) / 60 for t in times]  # Convert to minutes
        ax[i].clear()
        ax[i].plot(times, latencies, 'b-')
        ax[i].set_title(f'Ping Latency for {host}')
        ax[i].set_xlabel('Time (minutes)')
        ax[i].set_ylabel('Latency (ms)')
        ax[i].set_ylim(bottom=0)
        ax[i].grid(True)

        # Add summary statistics to the plot
        summary_text = f"Min: {summary_data[host]['min']:.2f}ms\n"
        summary_text += f"Max: {summary_data[host]['max']:.2f}ms\n"
        summary_text += f"Avg: {summary_data[host]['avg']:.2f}ms\n"
        summary_text += f"Loss: {summary_data[host]['loss']:.2f}%\n"
        summary_text += f"DNS: {dns_data[host]}\n"
        summary_text += f"Last hop: {traceroute_data[host]}"
        ax[i].text(0.02, 0.98, summary_text, transform=ax[i].transAxes, verticalalignment='top', fontsize=8, bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    
    # Save the current plot
    plt.savefig(os.path.join(OUTPUT_DIR, 'latency_plot.png'))

# Start ping thread
ping_thread = threading.Thread(target=ping_thread)
ping_thread.start()

# Set up the plot
fig, ax = plt.subplots(len(HOSTS), 1, figsize=(12, 6 * len(HOSTS)))
if len(HOSTS) == 1:
    ax = [ax]

ani = FuncAnimation(fig, update_plot, interval=GRAPH_UPDATE_INTERVAL, cache_frame_data=False)
plt.show()

# Cleanup
ping_thread_stop.set()
ping_thread.join()
