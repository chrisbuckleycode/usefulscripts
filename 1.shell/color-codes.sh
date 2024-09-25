#!/bin/bash
##
## FILE: color-codes.sh
##
## DESCRIPTION: Prints table colors (in color) against hex codes. Useful for frontend and graphic design work.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: color-codes.sh
##

# Function to print colored text
print_color() {
    echo -e "| \e[38;5;$1m$2\e[0m | $3 |"
}

# Table header
echo "| Color Name  | Hex Code   |"
echo "|-------------|------------|"

# Array of colors and hex codes
colors=("Red" "Blue" "Green" "Yellow" "Orange" "Purple" "Pink" "Black" "White" "Gray" "Brown" "Cyan" "Magenta" "Silver" "Gold" "Teal" "Navy" "Maroon" "Olive" "Turquoise")
hex_codes=("#FF0000" "#0000FF" "#008000" "#FFFF00" "#FFA500" "#800080" "#FFC0CB" "#000000" "#FFFFFF" "#808080" "#A52A2A" "#00FFFF" "#FF00FF" "#C0C0C0" "#FFD700" "#008080" "#000080" "#800000" "#808000" "#40E0D0")

# ANSI color codes for mapping to closest available colors
color_mapping=(
  196 21 46 226 208 127 211 16 231 244 130 51 201 188 220 30 17 124 58 45
)

# Print each row with colored text
for ((i=0; i<${#colors[@]}; i++)); do
    color_name="${colors[$i]}"
    hex_code="${hex_codes[$i]}"
    
    # Map hex color to the closest ANSI color code
    ansi_code=${color_mapping[$i]}
    
    print_color $ansi_code "${color_name}" "${hex_code}"
done
