#!/bin/bash
##
## FILE: speed-test-global-average.sh
##
## DESCRIPTION: Same as speed-test-global.sh but with additional table (average stats from multiple tests, history written to csv).
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: speed-test-global-average.sh
##

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "jq is not installed. Please install jq to run this script."
    exit 1
fi

# CSV file to store historical data
CSV_FILE="speed_test_history.csv"

# Create CSV file if it doesn't exist
if [ ! -f "$CSV_FILE" ]; then
    echo "Timestamp,URL,Download Speed (MB/s),Time (s),Country" > "$CSV_FILE"
fi

# Test URLs
urls=(
    "http://ams.download.datapacket.com/100mb.bin"
    "http://fra.download.datapacket.com/100mb.bin"
    "http://lon.download.datapacket.com/100mb.bin"
    "http://zur.download.datapacket.com/100mb.bin"
)

# Function to get country from IP
get_country() {
    local ip=$1
    local country=$(curl -s "http://ip-api.com/json/${ip}?fields=country" | jq -r '.country')
    echo "$country"
}

# Function for spinning cursor animation
spinner() {
    local pid=$1
    local delay=0.1
    local spinstr='|/-\'
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

# Function to print table
print_table() {
    printf "%-50s %-20s %-15s %-15s\n" "URL" "$1" "$2" "Country"
    printf "%-50s %-20s %-15s %-15s\n" "$(printf '%0.s-' {1..50})" "$(printf '%0.s-' {1..20})" "$(printf '%0.s-' {1..15})" "$(printf '%0.s-' {1..15})"
    
    while IFS='|' read -r url speed_display time_total country; do
        printf "%-50s %-20s %-15s %-15s\n" "${url:0:50}" "$speed_display" "$time_total" "$country"
    done
}

# Array to store results
results=()

# Test each URL
for url in "${urls[@]}"; do
    # Get IP address from URL
    ip=$(echo "$url" | awk -F[/:] '{print $4}')
    
    # Get country
    country=$(get_country "$ip")
    
    # Start the download and capture curl statistics
    printf "%-50s" "${url:0:50}"
    (curl -o /dev/null -w "%{speed_download} %{time_total}" -s "$url" > /tmp/curl_stats.$$) &
    spinner $!
    
    # Read the statistics
    read -r speed_download time_total < /tmp/curl_stats.$$
    rm /tmp/curl_stats.$$
    
    # Convert speed to MB/s and round to 2 decimal places using awk
    speed_download=$(awk -v speed="$speed_download" 'BEGIN {printf "%.2f", speed / 1048576}')
    speed_display="${speed_download} MB/s"
    time_total=$(awk -v time="$time_total" 'BEGIN {printf "%.2f", time}')
    
    # Store results
    results+=("$url|$speed_display|$time_total s|$country")
    
    # Append to CSV file
    echo "$(date '+%Y-%m-%d %H:%M:%S'),$url,$speed_download,$time_total,$country" >> "$CSV_FILE"
    
    # Print results
    printf "%-20s %-15s %-15s\n" "$speed_display" "$time_total s" "$country"
done

echo -e "\nTable (in original order):"
printf '%s\n' "${results[@]}" | print_table "Download Speed" "Time"

echo -e "\nSorted Table (by descending download speed):"
printf '%s\n' "${results[@]}" | sort -t'|' -k2,2nr | print_table "Download Speed" "Time"

# Calculate averages and create the new table
echo -e "\nSorted Table (by descending average download speed):"
awk -F',' '
    NR > 1 {
        sum_speed[$2] += $3; 
        sum_time[$2] += $4; 
        count[$2]++; 
        country[$2] = $5
    } 
    END {
        for (url in sum_speed) {
            avg_speed = sum_speed[url] / count[url];
            avg_time = sum_time[url] / count[url];
            printf "%s|%.2f MB/s|%.2f s|%s\n", url, avg_speed, avg_time, country[url]
        }
    }
' "$CSV_FILE" | sort -t'|' -k2,2nr | print_table "Download Speed Avg." "Time Avg."
