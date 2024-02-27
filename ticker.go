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
	Symbol         string `json:"symbol"`
	Price          string `json:"price"`
	PriceChangePct string `json:"priceChangePercent"`
}

func main() {
	// Declare the common symbol
	symbol := "BTCUSDT"

	// Define the API URLs
	priceURL := fmt.Sprintf("https://api.binance.com/api/v3/ticker/price?symbol=%s", symbol)
	statsURL := fmt.Sprintf("https://api.binance.com/api/v3/ticker/24hr?symbol=%s", symbol)

	// Fetch the BTCUSDT price
	priceResp, err := http.Get(priceURL)
	if err != nil {
		fmt.Println("Error fetching price data:", err)
		os.Exit(1)
	}
	defer priceResp.Body.Close()

	// Parse the JSON response for price
	var tickerPrice TickerResponse
	if err := json.NewDecoder(priceResp.Body).Decode(&tickerPrice); err != nil {
		fmt.Println("Error decoding price JSON:", err)
		os.Exit(1)
	}

	// Fetch the BTCUSDT stats
	statsResp, err := http.Get(statsURL)
	if err != nil {
		fmt.Println("Error fetching stats data:", err)
		os.Exit(1)
	}
	defer statsResp.Body.Close()

	// Parse the JSON response for stats
	var tickerStats TickerResponse
	if err := json.NewDecoder(statsResp.Body).Decode(&tickerStats); err != nil {
		fmt.Println("Error decoding stats JSON:", err)
		os.Exit(1)
	}

	// Get the current date and time
	currentTime := time.Now().Format("2006-01-02 15:04:05")

	// Convert the price to a float with 2 decimal places
	priceFloat, err := strconv.ParseFloat(tickerPrice.Price, 64)
	if err != nil {
		fmt.Println("Error converting price to float:", err)
		os.Exit(1)
	}
	formattedPrice := fmt.Sprintf("%.2f", priceFloat)

	// Convert the price change percentage to a float with 1 decimal place
	priceChangePctFloat, err := strconv.ParseFloat(tickerStats.PriceChangePct, 64)
	if err != nil {
		fmt.Println("Error converting price change percentage to float:", err)
		os.Exit(1)
	}
	formattedPriceChangePct := fmt.Sprintf("%.1f", priceChangePctFloat)

	// Print the results as a table
	fmt.Printf("| %-19s | %-10s | %-15s | %-20s |\n", "Timestamp", "Symbol", "Price", "Price Change %")
	fmt.Printf("|---------------------|------------|-----------------|----------------------|\n")
	fmt.Printf("| %-19s | %-10s | %-15s | %-20s |\n", currentTime, tickerPrice.Symbol, formattedPrice, formattedPriceChangePct)
}
