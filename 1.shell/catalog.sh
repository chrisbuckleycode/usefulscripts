#!/bin/bash
##
## FILE: catalog.sh
##
## DESCRIPTION: Blueprint "book catalog" CRUD style application (no update functionality, all records are immutable).
##              Requires sqlite3 (sudo apt install sqlite3)
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: catalog.sh
##

# Check if sqlite3 is installed
if ! command -v sqlite3 &> /dev/null
then
    echo "sqlite3 is not installed. Please install it and try again."
    exit 1
fi

# Database file
DB_FILE="home_library.db"

# Create table if not exists
sqlite3 "$DB_FILE" <<EOF
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_surname TEXT,
    author_initials TEXT,
    title TEXT,
    year INTEGER
);
EOF

# Function to clear screen and print header
function print_header() {
    clear
    echo "========================================"
    echo "       Home Library Catalog"
    echo "========================================"
    echo
}

# Function to browse individual record
function browse_individual_record() {
    local id=$1
    local record=$(sqlite3 -line "$DB_FILE" "SELECT * FROM books WHERE id = $id;")
    if [ -n "$record" ]; then
        echo "$record"
    else
        echo "No record found with ID $id."
    fi
}

# Function to browse records
function browse_records() {
    while true; do
        print_header
        echo "Book List:"
        echo "--------------------------------------"
        sqlite3 -column -header "$DB_FILE" "SELECT * FROM books;"
        echo
        echo "Options:"
        echo "- Press <Enter> to return to the main menu"
        echo "- Enter a book ID to view details"
        read -p "Your choice: " choice

        if [ -z "$choice" ]; then
            return
        elif [[ "$choice" =~ ^[0-9]+$ ]]; then
            print_header
            echo "Book Details:"
            echo "--------------------------------------"
            browse_individual_record "$choice"
            echo
            read -p "Press Enter to continue..."
        else
            echo "Invalid input. Please enter a valid numeric ID or press <Enter>."
            read -p "Press Enter to continue..."
        fi
    done
}

# Function to validate input
function validate_input() {
    local input="$1"
    if [[ "$input" =~ [[:alnum:]] ]]; then
        return 0
    else
        return 1
    fi
}

# Function to get valid input
function get_valid_input() {
    local prompt="$1"
    local input=""
    while true; do
        read -p "$prompt" input
        if [ "$input" = "." ]; then
            echo "ABORT"
            return 1
        elif validate_input "$input"; then
            echo "$input"
            return 0
        else
            echo "Error: Input must contain at least one alphanumeric character. Please try again." >&2
        fi
    done
}

# Function to add a new record
function add_record() {
    print_header
    echo "Add New Book:"
    echo "--------------------------------------"
    echo "Note: Enter a single period (.) to abort at any time."
    echo
    
    surname=$(get_valid_input "Author Surname: ")
    if [ "$surname" = "ABORT" ]; then
        echo "Aborting add record process..."
        sleep 1
        return
    fi
    
    initials=$(get_valid_input "Author Initials: ")
    if [ "$initials" = "ABORT" ]; then
        echo "Aborting add record process..."
        sleep 1
        return
    fi
    
    title=$(get_valid_input "Book Title: ")
    if [ "$title" = "ABORT" ]; then
        echo "Aborting add record process..."
        sleep 1
        return
    fi
    
    while true; do
        year=$(get_valid_input "Year of Publication: ")
        if [ "$year" = "ABORT" ]; then
            echo "Aborting add record process..."
            sleep 1
            return
        elif [[ "$year" =~ ^[0-9]+$ ]]; then
            break
        else
            echo "Error: Year must be a number. Please try again." >&2
        fi
    done

    sqlite3 "$DB_FILE" "INSERT INTO books (author_surname, author_initials, title, year) VALUES ('$surname', '$initials', '$title', $year);"
    echo "Book added successfully!"
    read -p "Press Enter to continue..."
}

# Function to delete a record
function delete_record() {
    while true; do
        print_header
        echo "Delete Book:"
        echo "--------------------------------------"
        sqlite3 -column -header "$DB_FILE" "SELECT * FROM books;"
        echo
        echo "Press <Enter> alone to return to the main menu"
        read -p "Enter the ID of the book to delete: " id

        if [ -z "$id" ]; then
            echo "Returning to main menu..."
            sleep 1
            return
        fi

        if [[ "$id" =~ ^[0-9]+$ ]]; then
            if sqlite3 "$DB_FILE" "SELECT EXISTS(SELECT 1 FROM books WHERE id = $id);" | grep -q 1; then
                sqlite3 "$DB_FILE" "DELETE FROM books WHERE id = $id;"
                echo "Book deleted successfully!"
                read -p "Press Enter to continue..."
                return
            else
                echo "Error: No book found with ID $id."
                read -p "Press Enter to try again..."
            fi
        else
            echo "Error: Invalid input. Please enter a valid numeric ID."
            read -p "Press Enter to try again..."
        fi
    done
}

# Main menu
while true; do
    print_header
    echo "1. Browse Records"
    echo "2. Add New Record"
    echo "3. Delete Record"
    echo "4. Exit"
    echo
    read -p "Enter your choice (1-4): " choice

    case $choice in
        1) browse_records ;;
        2) add_record ;;
        3) delete_record ;;
        4) echo "Goodbye!"; exit 0 ;;
        *) echo "Invalid choice. Please try again."; read -p "Press Enter to continue..." ;;
    esac
done
