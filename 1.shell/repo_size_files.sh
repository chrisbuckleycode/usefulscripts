#!/bin/bash
##
## FILE: repo_size_files.sh
##
## DESCRIPTION: Lists a repo's files sorted by size descending.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: repo_size_files.sh <clone_url>
##

# Error handling
if [ -z "$1" ]
then
  echo "Error: No URL provided. Please provide a URL as the first argument."
  exit 1
fi

# First argument is the git clone url
url=$1

# temp, to be cleaned up later
tmp_dir=$(mktemp -d -t git-clone-XXXXXX)

# Clone the URL into the temporary directory
git clone $url $tmp_dir

# List the files in order of size descending and output a table of filename and size
echo "Filename Size"
ls -lhS $tmp_dir | awk '{print $9, $5}' | column -t

# Remove the temporary directory
rm -rf $tmp_dir
