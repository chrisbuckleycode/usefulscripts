#!/usr/bin/env bash

# Parses netstat output to give
# a table of Local Port; PID/Program name
# (sorted by port)
# Run script with sudo

# Check if running with sudo
if [ "$(id -u)" != "0" ]; then
    echo "Please run this script with sudo."
    exit 1
fi

# Run netstat command and store the output
output=$(netstat -tulpn)

# Print table headers
printf "%-20s %-20s\n" "Local Port" "PID/Program name"
echo "---------------------------------------"

# Process each line of output (ignoring the first two lines)
counter=0
while IFS= read -r line; do
    ((counter++))

    # Skip the first two lines
    if [ "$counter" -le 2 ]; then
        continue
    fi

    # Extract Local Address, Process ID, and Program name
    local_address=$(echo "$line" | awk '{print $4}')
    process_id=$(echo "$line" | awk '{print $6}')
    program_name=$(echo "$line" | awk '{print $7}')

    # Extract port number from Local Address
    port=$(echo "$local_address" | awk -F ':' '{print $NF}')

    # Determine the correct PID/Program name based on the condition
    if [[ $process_id =~ ^[0-9] ]]; then
        pid_program=$process_id
    else
        pid_program=$program_name
    fi

    # Strip off any trailing colons from pid_program
    pid_program=${pid_program%%:*}

    # Print the formatted table row
    printf "%-20s %-20s\n" "$port" "$pid_program"
done <<< "$output" | sort -n -k1
