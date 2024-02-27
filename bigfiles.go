// This script will scan all files in your home directory (or just the Downloads folder) and then list them in order of descending size using less.
// Where possible, this is a more pure Go solution that doesn't rely on shell commands, instead using packages like os, io.
// However, scrollable output does indeed use local pager "less". This is a simpler alternative to a pure Go solution (tui package or otherwise).
// Tested on Linux (Ubuntu) only.
//
// Instructions:
// go mod init example.com/bigfiles
// go mod tidy
// go run bigfiles.go

package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"sort"
	"strings"
)

// Define a struct to hold file information
type File struct {
	Name string
	Size float64
}

func main() {
	// Print the menu
	fmt.Println("\n\nList files in descending size order")
	fmt.Println("Choose an option below and press the Enter key.")
	fmt.Println("\n!!!! IMPORTANT !!!!!")
	fmt.Println("Press Ctrl-C to cancel at any time!")
	fmt.Println("!!!! IMPORTANT !!!!!\n")
	fmt.Println("  1) All files in home directory  -WARNING, may take time, also no TOTALs")
	fmt.Println("  2) Downloads folder only")
	fmt.Println("  3) operation 3")
	fmt.Println("  4) operation 4")

	// Read the user's choice
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter your choice: ")
	choice, _ := reader.ReadString('\n')
	choice = strings.TrimSpace(choice)

	// Execute the appropriate action based on the user's choice
	switch choice {
	case "1":
		listFilesInOrder(os.Getenv("HOME"))
	case "2":
		listFilesInOrder(filepath.Join(os.Getenv("HOME"), "Downloads"))
	case "3":
		fmt.Println("You chose Option 3")
	case "4":
		fmt.Println("You chose Option 4")
	default:
		fmt.Println("\n\n!! Invalid input!!")
		fmt.Println("!! Invalid input!!")
		fmt.Println("!! Invalid input!! , choose again or Ctrl-C to exit")
		main()
	}
}

// listFilesInOrder lists all files in the given directory and its sub-directories in descending order of size
func listFilesInOrder(dir string) {
	// Create a slice to hold the file information
	var fileInfo []File

	// Walk the directory tree
	filepath.WalkDir(dir, func(path string, d os.DirEntry, err error) error {
		if !d.IsDir() {
			info, _ := d.Info()
			// Convert the size from bytes to megabytes
			sizeInMB := float64(info.Size()) / 1024.0 / 1024.0
			fileInfo = append(fileInfo, File{path, sizeInMB})
		}
		return nil
	})

	// Sort the files by size in descending order
	sort.Slice(fileInfo, func(i, j int) bool {
		return fileInfo[i].Size > fileInfo[j].Size
	})

	// Create a temporary file
	tmpfile, err := os.CreateTemp("", "example")
	if err != nil {
		panic(err)
	}
	defer os.Remove(tmpfile.Name()) // clean up

	// Write the file sizes and paths to the temporary file
	for _, file := range fileInfo {
		fmt.Fprintf(tmpfile, "%.2f MB: %s\n", file.Size, file.Name)
	}

	// Close the temporary file
	if err := tmpfile.Close(); err != nil {
		panic(err)
	}

	// Open the temporary file with "less"
	cmd := exec.Command("less", tmpfile.Name())
	cmd.Stdout = os.Stdout
	cmd.Stdin = os.Stdin
	cmd.Run()
}
