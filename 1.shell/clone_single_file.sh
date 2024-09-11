#!/bin/bash
##
## FILE: clone_single_file.sh
##
## DESCRIPTION: Clones a repo and concatenates all files with a specified extension with separators.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: clone_single_file.sh
##

# Get the current directory
current_dir=$(dirname "$0")

# Prompt for git clone URL
read -p "Enter the Git clone URL (HTTPS): " clone_url

# Check if the inputted URL is valid
if [[ ! "$clone_url" =~ ^https.*git$ ]]; then
    echo "Invalid Git clone URL. Please make sure it starts with 'https' and ends with 'git'."
    exit 1
fi

# Prompt for file extension
read -p "Enter the file extension (sh, py, or ALL): " extension

# Create a temporary directory
temp_dir=$(mktemp -d)
output_dir="$temp_dir/repo"

# Clone the repository
git clone "$clone_url" "$output_dir"

# Set the output file name
timestamp=$(date +"%Y%m%d%H%M%S")
output_file="$current_dir/cloned-single-file-$extension-$timestamp.txt"

# Find and concatenate files based on the extension
if [[ "$extension" == "ALL" ]]; then
    find "$output_dir" -type f -exec cat {} \; -exec echo "# FILE SEPARATOR" \; >> "$output_file"
else
    find "$output_dir" -type f -name "*.$extension" -exec cat {} \; -exec echo "# FILE SEPARATOR" \; >> "$output_file"
fi

# Print the path to the output file
echo "Cloned repository files have been joined into $output_file"

# Remove the temporary directory
rm -rf "$temp_dir"
