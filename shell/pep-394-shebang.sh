#!/bin/bash
##
## FILE: pep-394-shebang.sh
##
## DESCRIPTION: Updates Python scripts with PEP-394 comcompliant shebang line.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: pep-394-shebang.sh
##

# Function to update the shebang line in a Python file
update_shebang() {
    file="$1"
    shebang_found=false

    while IFS= read -r line; do
        if [[ "$line" == '#!/usr/bin/env python3' ]]; then
            echo "Updating shebang in $file"
            sed -i '1s|^#!/usr/bin/env python3$|#!/usr/bin/env python|' "$file"
            shebang_found=true
            break
        elif [[ "$line" == '#!/usr/bin/env python' ]]; then
            shebang_found=true
            break
        fi
    done < "$file"

    if [[ "$shebang_found" == false ]]; then
        echo "Inserting shebang in $file"
        sed -i '1i\
#!/usr/bin/env python\n
' "$file"
    fi
}

# Traverse current directory and subdirectories for Python files excluding .env directories
find . -type d -name '.env' -prune -o -type f -name '*.py' -print | while read -r file; do
    update_shebang "$file"
done
