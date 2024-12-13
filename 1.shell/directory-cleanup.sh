#!/bin/bash
##
## FILE: directory-cleanup.sh
##
## DESCRIPTION: Traverses sub-directories and deletes cache folders.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: directory-cleanup.sh
##

# Initialize an array to store directories to be deleted
declare -a dirs_to_delete

# Traverse one level below the current directory
for dir in */; do
    # Check for .env, .venv, and .terraform directories
    for target in ".env" ".venv" ".terraform"; do
        if [ -d "${dir}${target}" ]; then
            dirs_to_delete+=("${dir}${target}")
        fi
    done
done

# Check if any directories were found
if [ ${#dirs_to_delete[@]} -eq 0 ]; then
    echo "No directories found to delete."
    exit 0
fi

# Display the list of directories to be deleted
echo "Directories to be deleted:"
printf '%s\n' "${dirs_to_delete[@]}"

# Ask for user confirmation
read -p "Do you want to delete these directories? (y/yes or n/no): " user_input

# Convert user input to lowercase
user_input_lower=$(echo "$user_input" | tr '[:upper:]' '[:lower:]')

# Process based on user input
if [[ "$user_input_lower" == "y" || "$user_input_lower" == "yes" ]]; then
    # Delete the directories
    for dir in "${dirs_to_delete[@]}"; do
        rm -rf "$dir"
        echo "Deleted: $dir"
    done
    echo "Deletion complete."
else
    echo "Operation cancelled. No files were deleted."
fi