#!/usr/bin/env bash

# Clone all gists WITHOUT using API tokens
# Requires gh cli (authenticated)


# Check if 'gh' command exists
if ! command -v gh &> /dev/null; then
    echo "Error: 'gh' command is not installed. Please install the GitHub CLI (https://cli.github.com/) and try again."
    exit 1
fi

# Check if 'zip' command exists
if ! command -v zip &> /dev/null; then
    echo "Error: 'zip' command is not installed. Please install the 'zip' package and try again."
    exit 1
fi

# Check if 'gist-backups' directory exists, create it if not
backup_parent_dir="./gist-backups"
if [ ! -d "$backup_parent_dir" ]; then
    mkdir "$backup_parent_dir"
fi

# Create a directory with the current date and time
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
timestamp_dir="$backup_parent_dir/$timestamp"
mkdir "$timestamp_dir"

# Get list of gist IDs
gist_list=$(gh gist list -L 999 | awk 'NR>1 {print $1}')

# Clone gists and store file paths in an array
cloned_files=()
for gist_id in $gist_list; do
    clone_url="https://gist.github.com/$gist_id.git"
    gh gist clone "$clone_url" "$timestamp_dir/$gist_id"
    cloned_files+=("$timestamp_dir/$gist_id")
done

# Compress the cloned gists into a single zip file
zip -r "$timestamp_dir/archive.zip" "${cloned_files[@]}"

# Delete the individual files
for file in "${cloned_files[@]}"; do
    rm -rf "$file"
done

echo "Cloning and archiving completed successfully."
