#!/usr/bin/env bash

url="https://www.eff.org/files/2016/09/08/eff_short_wordlist_1.txt"
# Wordlist explanation: https://www.eff.org/dice

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

# Set the desired number of words in the passphrase - each word worth approx. 10 bits of entropy
num_words=6

# Loop to generate and print five random passphrases
for ((i=1; i<=5; i++)); do
    passphrase=""
    for ((j=1; j<=num_words; j++)); do
        # Generate random line number
        line=$(od -An -N2 -i /dev/urandom | awk -v n="$num_lines" '{print $1 % n + 1}')

        # Get the randomly selected word from the dictionary file
        word=$(sed -n "${line}p" "$dictionary_file_cut")

        # Append the word to the passphrase
        if [ "$j" -eq 1 ]; then
            passphrase="$word"
        else
            passphrase="$passphrase-$word"
        fi
    done

    # Print the passphrase
    echo "Passphrase $i: $passphrase"
done
