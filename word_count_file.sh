#!/usr/bin/env bash

# word count script
#
# usage: ./script.sh filetoparse.txt
# alternative usage: curl -sS <URL> | ./script.sh -
#
# one-liner at bottom of file


# Check if a filename was provided as an argument
if [ -z "$1" ]; then
    echo "Please provide a filename as the first argument."
    exit 1
fi

# Print the header row
printf "%-20s %s\n" "WORD" "FREQUENCY"

# Parse the file and output the results
awk '
    BEGIN {
        # Set the field separator to non-word characters
        FS="[^a-zA-Z0-9]+"
    }
    {
        # Loop through each field (word) in the line
        for (i = 1; i <= NF; i++) {
            # Only count non-empty fields as words
            if (length($i) > 0) {
                # Increment the count for the word
                words[tolower($i)]++
            }
        }
    }
    END {
        # Loop through the words array and print the results - limit to 20 results (handy for long files that use entire terminal buffer)
        for (word in words) {
            if (++counter > 20) break
            printf "%-20s %d\n", word, words[word]
        }
    }
' "$1" | sort -k2,2nr -k1,1d | column -t


# one-liner copy and paste command
# printf "%-20s %s\n" "WORD" "FREQUENCY"; awk 'BEGIN {FS="[^a-zA-Z0-9]+"} {for (i = 1; i <= NF; i++) {if (length($i) > 0) {words[tolower($i)]++}}} END {for (word in words) {printf "%-20s %d\n", word, words[word]}}' readme.txt | sort -k2,2nr -k1,1d | column -t
