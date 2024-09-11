#!/bin/bash
##
## FILE: random_digits.sh
##
## DESCRIPTION: Randomly generates 3-digit numbers (10 instances each run).
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: random_digits.sh
##

# Loop to print 10 random numbers
for ((i=0; i<10; i++)); do
    # Generate a random number between 0 and 999
    random_num=$(printf "%03d" $((RANDOM % 1000)))
    
    # Print the random number
    echo $random_num
done
