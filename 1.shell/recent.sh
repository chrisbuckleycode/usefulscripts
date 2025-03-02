#!/bin/bash
##
## FILE: recent
##
## DESCRIPTION: Displays 9 most recently modified txt files found recursively from $HOME.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: Copy to ~/.local/bin or elsewhere in your PATH and rename to "recent".
##

# Find the 20 most recently modified .txt files, excluding hidden dirs
readarray -t files < <(find "$HOME" -type f -name "*.txt" -not -path "*/\.*/*" -printf "%T@ %p\n" 2>/dev/null | sort -nr | head -n 20 | cut -d' ' -f2-)

# Number and display files relative to home directory
for i in "${!files[@]}"; do
    rel_path="${files[i]#$HOME/}"
    echo "$((i+1)). $rel_path"
done

# Get user input
read -p "Enter file number to open (1-${#files[@]}): " num

# Validate input
if [[ "$num" =~ ^([1-9]|1[0-9]|20)$ ]] && [ "$num" -le "${#files[@]}" ]; then
    # Open file in xed without waiting
    xed "${files[$((num-1))]}" &
else
    echo "Invalid selection"
    exit 1
fi

exit 0
