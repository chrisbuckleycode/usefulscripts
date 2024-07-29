#!/usr/bin/env bash

# Generate 20 random permutations of adjective-noun names e.g. "Cool Luke"
# Requires your own source files: adjectives.txt, nouns.txt
# Adjectives currently limited to maximum 10 characters for brevity

adjectives_file="adjectives.txt"
nouns_file="nouns.txt"

# Check if adjectives.txt and nouns.txt exist
if [ ! -f "$adjectives_file" ]; then
    echo "Error: $adjectives_file not found. Please create the adjectives file."
    exit 1
fi

if [ ! -f "$nouns_file" ]; then
    echo "Error: $nouns_file not found. Please create the nouns file."
    exit 1
fi

# Read adjectives and nouns into arrays
adjectives=($(cat "$adjectives_file" | awk 'length($0) <= 10' | shuf))
nouns=($(cat "$nouns_file" | shuf))

for ((i=0; i<20; i++))
do
    random_adj=${adjectives[$i]}
    random_noun=${nouns[$i]}
    echo "$random_adj-$random_noun"
done
