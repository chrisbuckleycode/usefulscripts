#!/bin/bash
##
## FILE: speed-test-global.sh
##
## DESCRIPTION: Internet speed test. Downloads test file from multiple sites and displays speed/time/country stats in a table.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: speed-test-global.sh
##

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "jq is not installed. Please install jq to run this script."
    exit 1
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
    printf "%-50s %-20s %-15s %-15s\n" "URL" "Download Speed" "Time" "Country"
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
    time_total=$(awk -v time="$time_total" 'BEGIN {printf "%.2f s", time}')
    
    # Store results
    results+=("$url|$speed_display|$time_total|$country")
    
    # Print results
    printf "%-20s %-15s %-15s\n" "$speed_display" "$time_total" "$country"
done

echo -e "\nTable (in original order):"
printf '%s\n' "${results[@]}" | print_table

echo -e "\nSorted Table (by descending download speed):"
printf '%s\n' "${results[@]}" | sort -t'|' -k2,2nr | print_table
