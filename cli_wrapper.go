// Basic golang CLI
// Uses Golang "subcommands" to demonstrate Linux command aliasing.
// Update the variable to add new (external) commands.
// Can be used for more advanced use cases e.g. own CLI for frequently-made cloud API calls.
// Recommend placing the built executable in your $PATH.
//
// Build Instructions:
// go build -o easy cli_wrapper.go
//
// Usage:
// ./easy help

package main

import (
	"fmt"
	"os"
	"os/exec"
)

var subcommands = map[string]string{
	"recent": "List files in the current directory (sorted by modification time, most recent last)",
	"env":    "Display environment variables",
	"host":   "Display hostname",
	"help":   "Display this help message",
}

func main() {
	// Check if a subcommand is provided, if not then display help
	if len(os.Args) < 2 {
		displayHelp()
		return
	}

	// Handle subcommands
	switch os.Args[1] {
	case "recent":
		executeCommand("ls", "-haltr")
	case "env":
		executeCommand("printenv")
	case "host":
		fmt.Println("Hostname:", getHostname())
	case "help":
		displayHelp()
	default:
		fmt.Println("Unknown subcommand. Use 'easy help' to see available commands.")
	}
}

// Executes the given command with the provided arguments
func executeCommand(command string, args ...string) {
	cmd := exec.Command(command, args...)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	err := cmd.Run()
	if err != nil {
		fmt.Printf("Failed to execute command: %v\n", err)
	}
}

// Retrieves the hostname
func getHostname() string {
	hostname, err := os.Hostname()
	if err != nil {
		fmt.Printf("Failed to retrieve hostname:", err)
		return "" // Return an empty string in case of error
	}
	return hostname
}

// Shows the help message
func displayHelp() {
	fmt.Println("Usage: easy <command>")
	fmt.Println("Available commands:")

	for cmd, desc := range subcommands {
		fmt.Printf("  easy %s - %s\n", cmd, desc)
	}
}
