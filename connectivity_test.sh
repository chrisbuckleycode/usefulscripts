#!/usr/bin/env bash

# Conduct an internet connectivity test using curl and display statistics
# calculated from the samples gathered, specifically speed in kilobytes per second

# Set the number of samples to take
samples=10

# Set the URL to download from
url=http://speedtest.tele2.net/10MB.zip

# Conduct the test and calculate the statistics
for i in $(seq 1 $samples); do
    curl -w "%{speed_download}\\n" -o /dev/null --progress-bar $url
done | awk -v samples=$samples '{
    a[i++]=$0;
    s+=$0
} END {
    m=s/samples;
    for (j in a) ss+=((a[j]-m)^2);
    asort(a);
    print "min: "a[1]/1024,"KB/s";
    print "max: "a[samples]/1024,"KB/s";
    print "mean: "m/1024,"KB/s";
    print "stdev: "sqrt(ss/samples)/1024,"KB/s"
}'


# one-liner version
# for i in {1..10}; do curl -w "%{speed_download}\\n" -o /dev/null --progress-bar http://speedtest.tele2.net/10MB.zip; done | awk '{a[i++]=$0;s+=$0}END{m=s/i;for(j in a)ss+=((a[j]-m)^2);asort(a);print "min: "a[1]/1024,"KB/s\nmax: "a[i-1]/1024,"KB/s\nmean: "m/1024,"KB/s\nstdev: "sqrt(ss/i)/1024,"KB/s"}'
