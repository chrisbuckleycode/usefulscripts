#!/usr/bin/env bash

# fetches a random lyric by The Killers (or a band of your choice)
# also can use this one-liner copy and paste terminal command:
# curl -sS -X GET "https://songsexcerpt.mohd.app/api/v1/getRandomExcerpt?artists=231" | jq -r 'to_entries[] | [.key, .value] | @tsv' | sed 's/\\n/. /g'


# Set the URL
url="https://songsexcerpt.mohd.app/api/v1/getRandomExcerpt?artists=231"

# Send the GET request using curl
response=$(curl -sS -X GET "$url")

# Parse the JSON response and convert it into a two-column table
table=$(echo "$response" | jq -r 'to_entries[] | [.key, .value] | @tsv')

# Replace instances of \n with .  in the table
table=$(echo "$table" | sed 's/\\n/. /g')

# Print the resulting table
echo "$table"
