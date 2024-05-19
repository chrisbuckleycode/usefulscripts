#!/usr/bin/env bash

# Prompt user to run the script as sudo
echo "This script must be run as sudo."
echo "This script assumes you have no existing file: /etc/X11/xorg.conf."
echo "---"
echo "Press any key to continue or Ctrl-C to quit."
read -n 1 -s

# Check if the prerequisite symbolic link /sys/class/backlight/intel_backlight exists
if [ ! -L "/sys/class/backlight/intel_backlight" ]; then
  echo "Error: /sys/class/backlight/intel_backlight does not exist."
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

# Create the file with the defined contents
echo "$file_contents" > "$filename"

# Display a success message
echo "File created: $filename"

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
