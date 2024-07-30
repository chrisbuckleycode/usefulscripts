# This script will search the current directory and all sub-directories
# for .py files, grepping any function declarations
# and saving to a text file
# so you can look at a list of functions by name
# which might be good for ideas of how to compose your own functions
# Run this from the directory where you clone all your git repos to

import os
import fnmatch

def find_files(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def grep_lines(files, string):
    result = []
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                if string in line:
                    result.append(line.lstrip("# "))
    return result

def write_lines(lines, filename):
    lines.sort()
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)

    with open(filename, 'w') as f:
        last_line = None
        for line in lines:
            if line != last_line:
                f.write(line)
                last_line = line


# Find all .py files in the current directory and subdirectories
files = find_files('*.py', '.')

# Grep lines containing "def ", remove leading spaces and comment markers
lines = grep_lines(files, 'def ')

# Sort alphabetically, write the lines to a file (only if not duplicates)
write_lines(lines, 'functions.txt')
