import os
import hashlib
from collections import Counter
from prettytable import PrettyTable

# Initialize empty dictionary to store file path and md5 checksum
file_dict = {}

# Get home directory
home_dir = os.path.expanduser("~/")

# Get all non-hidden directories in home directory
directories = [home_dir] + [os.path.join(home_dir, d) for d in os.listdir(home_dir) if os.path.isdir(os.path.join(home_dir, d)) and not d.startswith(".")]

# Loop through all directories
for directory in directories:
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Restrict by file extension
            if file.endswith(("jpg", "jpeg", "gif", "png")):
                # Get full file path
                file_path = os.path.join(root, file)
                print(f"Calculating md5 checksum for {file_path}")
                # Open file and calculate md5 checksum
                with open(file_path, "rb") as f:
                    md5 = hashlib.md5(f.read()).hexdigest()
                # Add file path and md5 checksum to dictionary
                file_dict[file_path] = md5

# Create counter from dictionary values
counter = Counter(file_dict.values())

# Create new dictionary with key value pairs whose counter value is greater than 1
duplicate_files = {k: v for k, v in file_dict.items() if counter[v] > 1}

# Print duplicate files in a table
table = PrettyTable()
table.field_names = ["File Path", "MD5 Checksum"]
for file_path, md5 in sorted(duplicate_files.items(), key=lambda x: x[1]):
    table.add_row([file_path, md5])
print(table)
