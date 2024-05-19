#!/usr/bin/env bash

# Script to allow command-line brightness control for Intel graphics display on Linux
# This permits setting backlight as low as 1 and incrementing/decrementing in single digit steps
# (ordinarily only steps of 10 are available via button press and minimum value of 10)


# Prompt user to run the script as sudo
echo "This script must be run as sudo."
echo "---"
echo "Press any key to continue or Ctrl-C to quit."
read -n 1 -s

# Check if the prerequisite symbolic link /sys/class/backlight/intel_backlight exists
if [ ! -L "/sys/class/backlight/intel_backlight" ]; then
  echo "Error: /sys/class/backlight/intel_backlight does not exist."
  echo "Exiting..."
  exit 1
fi

# Define the filename and path
filename="/etc/X11/xorg.conf"

# Define the file contents
file_contents='Section "Device"
    Identifier  "Intel Graphics"
    Driver      "intel"
    Option      "Backlight"  "intel_backlight"
EndSection'

# Check if the file already exists
if [ -f "$filename" ]; then
  # Check if the string "intel_backlight" exists in the file
  if grep -q "intel_backlight" "$filename"; then
    echo "Check config: An entry for intel_backlight already exists and will be presumed in working order."
  else
    # Add file_contents to the file
    echo "$file_contents" >> "$filename"
    echo "File updated: $filename"
  fi
else
  # Create the file with the defined contents
  echo "$file_contents" > "$filename"
  echo "File created: $filename"
fi

# Check if xbacklight is installed
if ! command -v xbacklight &> /dev/null; then
    echo "xbacklight is not installed. Installing..."
    apt install xbacklight -y
    echo "xbacklight installed successfully."
fi

# Display completion message and instructions
echo "Log off and log on to complete installation"
echo "To set minimum brightness, run \"xbacklight -set 1\""
echo "To increase brightness, run \"xbacklight -inc 1\""
echo "To decrease brightness, run \"xbacklight -dec 1\""
