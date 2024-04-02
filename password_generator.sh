#!/usr/bin/env bash

# Password generator to create 3-word passphrases using the EFF short wordlist.
# Words "randomly" selected using urandom.
# Made for demo purposes, no warranties made for security of passphrases!

url="https://www.eff.org/files/2016/09/08/eff_short_wordlist_2_0.txt"

dictionary_file="words.txt"
dictionary_file_cut="words_cut.txt"

# Check if the file already exists locally
if [ -f "$dictionary_file" ]; then
    echo "File already exists. Skipping download."
else
    # Download the wordlist file
    curl -o words.txt "$url"
fi

# Extract the second column
cut -f 2- "$dictionary_file" > "$dictionary_file_cut"

# Count the number of lines in the dictionary file
num_lines=$(wc -l < "$dictionary_file_cut")

# Loop to generate and print five random passphrases
for ((i=1; i<=5; i++)); do
    # Generate random line numbers
    line1=$(od -An -N2 -i /dev/urandom | awk -v n="$num_lines" '{print $1 % n + 1}')
    line2=$(od -An -N2 -i /dev/urandom | awk -v n="$num_lines" '{print $1 % n + 1}')
    line3=$(od -An -N2 -i /dev/urandom | awk -v n="$num_lines" '{print $1 % n + 1}')

    # Get the randomly selected words from the dictionary file
    word1=$(sed -n "${line1}p" "$dictionary_file_cut")
    word2=$(sed -n "${line2}p" "$dictionary_file_cut")
    word3=$(sed -n "${line3}p" "$dictionary_file_cut")

    # Print the randomly selected words separated by hyphens
    echo "Passphrase $i: $word1-$word2-$word3"
done
