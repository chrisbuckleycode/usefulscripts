#!/bin/bash
##
## FILE: git_cloner.sh
##
## DESCRIPTION: Clones all git repos in a Github account without using API tokens (requires gh cli).
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: git_cloner.sh
##

# Requires gh cli already authenticated

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

# Check if 'git-backups' directory exists, create it if not
backup_parent_dir="./git-backups"
if [ ! -d "$backup_parent_dir" ]; then
    mkdir "$backup_parent_dir"
fi

# Create a directory with the current date and time
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
timestamp_dir="$backup_parent_dir/$timestamp"
mkdir "$timestamp_dir"

# Get the user ID (strictly not required for cloning but will make file operations easier)
gh_user=$(gh api user -q ".login")

# Get list of git names but strip out user prefix
git_list=$(gh repo list | awk '{print $1}' | sed "s/^$gh_user\///")

# Clone gits and store file paths in an array
cloned_files=()
for git_id in $git_list; do
    clone_url="https://github.com/$gh_user/$git_id.git"
    gh repo clone "$clone_url" "$timestamp_dir/$git_id"
    cloned_files+=("$timestamp_dir/$git_id")
done

# Compress the cloned gits into a single zip file
zip -r "$timestamp_dir/archive.zip" "${cloned_files[@]}"

# Delete the individual files
for file in "${cloned_files[@]}"; do
    rm -rf "$file"
done

echo "Cloning and archiving completed successfully."
