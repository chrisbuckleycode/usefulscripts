#!/bin/bash
##
## FILE: logon-disk-check.sh
##
## DESCRIPTION: Logon script to check file system usage/inodes and warn if >90%.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: Copy script to /etc/profile.d/
##

# Set threshold
THRESHOLD=90

# Check disk space usage
df -h | awk 'NR>1 {gsub(/%/,"",$5); if ($5 >= '"$THRESHOLD"') printf "\033[1;31mWARNING: Filesystem %s is at %s%% capacity (mounted on %s)\033[0m\n", $1, $5, $6}'

# Check inode usage
df -i | awk 'NR>1 {gsub(/%/,"",$5); if ($5 >= '"$THRESHOLD"') printf "\033[1;31mWARNING: Filesystem %s inode usage at %s%% (mounted on %s)\033[0m\n", $1, $5, $6}'
