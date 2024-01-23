// Fetches a random lyric by The Killers (or a band of your choice)
//
// Sends a GET request to the specified URL
// Parses the JSON response into a map
// Replaces instances of \n with .  in the values
// Prints each key-value pair as a line in a table
// Error handling included. If error when sending the GET request or reading the response body, the program will panic and print the error message
// Future feature: replce panic(err) with own error handling

// Instructions:
// go mod init example.com/lyrics-api-get
// go mod tidy
// go run lyrics_api_get.go

package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func main() {
	// Set the URL
	url := "https://songsexcerpt.mohd.app/api/v1/getRandomExcerpt?artists=231"

	// Send the GET request using http.Get
	resp, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	// Read the response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	// Parse the JSON response and convert it into a map
	var result map[string]interface{}
	json.Unmarshal(body, &result)

	// Iterate over the map and print each key-value pair as a line in a table
	for key, value := range result {
		// Replace instances of \n with . in the value
		strValue := strings.ReplaceAll(fmt.Sprintf("%v", value), "\\n", ". ")
		fmt.Printf("%s\t%s\n", key, strValue)
	}
}
