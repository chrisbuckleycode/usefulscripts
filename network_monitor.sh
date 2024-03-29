#!/usr/bin/env bash

LOG_FILE="./network_monitor.log"
PING_HOST="8.8.8.8"  # Change this to the IP or hostname you want to ping
TIMEOUT_SECONDS=1  # Timeout value in seconds, required to kill hanging tracepath

while true; do
    timestamp=$(date "+%Y-%m-%d %H:%M:%S")

    ping -c 1 $PING_HOST > /dev/null

    # If previous command has error code 0 i.e. if ping has no errors    
    if [ $? -eq 0 ]; then    # Use "-ne" for temporary testing
        echo "$timestamp - Network is connected" | tee -a "$LOG_FILE"
    else
        echo "$timestamp - Network disconnected" | tee -a "$LOG_FILE"
        
        # Additional commands to gather more information
        # Example: Run 'ip a' command to get network interface details
        echo "Network interface details:" >> $LOG_FILE
        ip a >> $LOG_FILE
        
        # Example: Run 'iwconfig' command to get wireless interface details
        echo "Wireless interface details:" >> $LOG_FILE
        iwconfig >> $LOG_FILE 2>&1    # capture both stdout and stderror
        
        # Example: Run 'dmesg' command to check recent system messages
        echo "Recent system messages:" >> $LOG_FILE
        dmesg | tail -n 10 >> $LOG_FILE
        
        # Example: Run 'tracepath' command with timeout
        echo "Tracepath to $PING_HOST:" >> $LOG_FILE
        timeout $TIMEOUT_SECONDS tracepath $PING_HOST >> $LOG_FILE
        
        # Add more commands as needed to gather additional information
        
        echo "----------------------------------------" >> $LOG_FILE
    fi
    
    sleep 1  # Adjust the sleep duration as needed
done
