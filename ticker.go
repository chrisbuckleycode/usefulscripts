package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"strconv"
	"time"
)

type TickerResponse struct {
	Symbol string `json:"symbol"`
	Price  string `json:"price"`
}

func main() {
	// Define the new API URL for BTCUSDT
	btcusdtURL := "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

	// Perform the GET request
	resp, err := http.Get(btcusdtURL)
	if err != nil {
		fmt.Println("Error fetching data:", err)
		os.Exit(1)
	}
	defer resp.Body.Close()

	// Parse the JSON response
	var ticker TickerResponse
	if err := json.NewDecoder(resp.Body).Decode(&ticker); err != nil {
		fmt.Println("Error decoding JSON:", err)
		os.Exit(1)
	}

	// Get the current date and time
	currentTime := time.Now().Format("2006-01-02 15:04:05")

	// Convert the price to a float with 2 decimal places
	priceFloat, err := strconv.ParseFloat(ticker.Price, 64)
	if err != nil {
		fmt.Println("Error converting price to float:", err)
		os.Exit(1)
	}
	formattedPrice := fmt.Sprintf("%.2f", priceFloat)

	// Print the results as a table
	fmt.Printf("| %-19s | %-10s | %-15s |\n", "Timestamp", "Symbol", "Price")
	fmt.Printf("|---------------------|------------|-----------------|\n")
	fmt.Printf("| %-19s | %-10s | %-15s |\n", currentTime, ticker.Symbol, formattedPrice)
}
