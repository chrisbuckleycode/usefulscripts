#!/bin/bash
##
## FILE: top100.sh
##
## DESCRIPTION: Displays 100 most frequently used commands from Zsh's history.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: top100.sh
##

# Directly specify the history file path
HISTFILE="$HOME/.zsh_history"

# Check if the history file exists
if [[ ! -f "$HISTFILE" ]]; then
    echo "History file does not exist."
    exit 1
fi

# Read the history, strip the first 15 characters, count occurrences, and sort
# i.e. show most frequently used at bottom
awk '{cmd[substr($0, 16)]++} END {for (c in cmd) print cmd[c], c}' "$HISTFILE" | sort -n | tail -n 100
