#!/bin/bash
##
## FILE: temps.sh
##
## DESCRIPTION: Records sensor temperature to a file for direct import into spreadsheet software.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: temps.sh
##

filename=~/sensor_log_$(date +"%FT%H%M%z").txt
# filename=test.txt
date +"%FT%H%M%z" >> $filename
printf "\n" >> $filename

while [ true ]
do
   printf "%s" "$(date +"+%F_%T   ")   " >> $filename
   sensors | awk '/^Package/{print $4}' |  awk 'BEGIN{ FIELDWIDTHS= "1 4 6"; OFS="|"}{$1=$1}1' >> $filename
   sleep 1
done
