#!/usr/bin/env bash

# Provide input file of sentences as argument, it will be sorted by sentence length and saved as a new file
# It basically creates and index, sorts by it, then removes it prior to saving


# Check if a filename is provided as an argument
if [ $# -eq 0 ]; then
  echo "Please provide a filename as an argument."
  exit 1
fi

input_file=$1
output_file="${input_file%.*}_sorted.${input_file##*.}"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
  echo "Input file '$input_file' does not exist."
  exit 1
fi

# Read the lines from the input file and store them in an array
lines=()
while IFS= read -r line; do
  lines+=("$line")
done < "$input_file"

# Sort the lines based on their length in descending order

# Use printf to separate each line with a newline character
formatted_lines=$(printf "%s\n" "${lines[@]}")

# Use awk to prepend each line with its length
lines_with_length=$(echo "$formatted_lines" | awk '{ print length, $0 }')

# Use sort to sort the lines based on the length in reverse numerical order
sorted_lines_with_length=$(echo "$lines_with_length" | sort -n)

# Use cut to remove the length column and keep only the lines
sorted_lines=$(echo "$sorted_lines_with_length" | cut -d" " -f2-)

# Write the sorted lines to the output file
printf "%s\n" "$sorted_lines" > "$output_file"

echo "Sorted lines have been saved to '$output_file'."
