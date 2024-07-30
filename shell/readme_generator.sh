#!/bin/bash
##
## FILE: readme_generator.sh
##
## DESCRIPTION: Generates a README.md from/for scripts in the current directory.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: readme_generator.sh
##

README="README-scratch.md"
SCRIPT_NAME=$(basename "$0")

# Remove existing README.md file
if [ -f "$README" ]; then
    rm "$README"
fi

# Loop through each .py and .sh file in the current directory
for file in *.py *.sh; do
    if [ -f "$file" ] && [ "$file" != "$SCRIPT_NAME" ]; then
        # Extract FILE and DESCRIPTION values
        file_key=$(grep "## FILE" "$file" | sed 's/## FILE: //')
        description_key=$(grep "## DESCRIPTION" "$file" | sed 's/## DESCRIPTION: //')

        # Append to README.md
        echo -e "## $file_key\n$description_key\n" >> "$README"
    fi
done