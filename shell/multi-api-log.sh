#!/bin/bash
##
## FILE: multi-api-log.sh
##
## DESCRIPTION: Requests from a randomly chosen API and writes response to log file.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: multi-api-log.sh
##

# Randomly curl an api and write the response to a log file
# Start the script in the background using: sudo ./multi-api-log.sh &
# Tail the logfile using: tail -f /var/log/quote.log
# Stop the script running using: sudo pkill -f ./multi-api-log.sh

# List of APIs
apis=(
  "https://zenquotes.io/api/random | jq -r '.[0].q'"
  "https://api.quotable.io/quotes/random | jq -r '.[0].content'"
  "https://stoic.tekloon.net/stoic-quote | jq -r '.data.quote'"
  # Add more APIs here
)

# Log file path
log_file="/var/log/quote.log"

# Main loop
while true; do
  # Choose a random API from the list
  api="${apis[RANDOM % ${#apis[@]}]}"

  # Make the request and extract the quote using jq
  quote=$(eval "curl -s $api")

  # Get the current date and time
  timestamp=$(date +"%Y-%m-%d %H:%M:%S")

  # Write the quote and timestamp to the log file
  echo "$timestamp  $quote" >> "$log_file"

  # Sleep for 15 seconds
  sleep 15
done
