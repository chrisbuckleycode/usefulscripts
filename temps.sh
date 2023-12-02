#!/usr/bin/env bash
# temps.sh
# this script will create a timestamped file and record temperature data every second to it.
# It is easily imported into Excel or LibreOffice Calc to make charts with.

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
