#!/bin/bash
##
## FILE: spinner.sh
##
## DESCRIPTION: Spinner animation functions and code.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: spinner.sh
##

# Useful when a process takes several seconds and shows no obvious progress to end user.
# Copy and paste functions to your script or place in a separate file and link
# e.g. "source lib.sh"


spinner() {
  local -r delay='0.1' # Delay between spinner frames in seconds
  local -r spinstr='|/-\' # Characters used for the spinner animation

  while :; do
    printf '\r%s ' "${spinstr:i++%${#spinstr}:1}"
    sleep "$delay"
  done
}

start_spinner() {
  spinner &
  spinner_pid=$!
}

stop_spinner() {
  kill "$spinner_pid"
  wait "$spinner_pid" 2>/dev/null
  printf '\r' # Clear the spinner line
  echo "Task complete!"
}

echo "Performing a long-running task..."
start_spinner

# Long-running task...
sleep 5

stop_spinner

