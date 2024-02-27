// Display crypto pair price data, updated every 60 seconds, uses Binance free API
//
// Instructions:
// go mod init example.com/ticker
// go mod tidy
// go run ticker.go

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

// fetchTickerData fetches data from the specified API URL
func fetchTickerData(url string) (TickerResponse, error) {
	resp, err := http.Get(url)
	if err != nil {
		return TickerResponse{}, err
	}
	defer resp.Body.Close()

	var ticker TickerResponse
	if err := json.NewDecoder(resp.Body).Decode(&ticker); err != nil {
		return TickerResponse{}, err
	}

	return ticker, nil
}

func printTableHeader() {
	fmt.Printf("| %-19s | %-10s | %-15s | %-20s |\n", "Timestamp", "Symbol", "USD Price", "24 Hr Price Change %")
	fmt.Printf("|---------------------|------------|-----------------|----------------------|\n")
}

func main() {
	// Declare the common symbol
	symbol := "BTCUSDT"

	// Define the API URLs
	priceURL := fmt.Sprintf("https://api.binance.com/api/v3/ticker/price?symbol=%s", symbol)
	statsURL := fmt.Sprintf("https://api.binance.com/api/v3/ticker/24hr?symbol=%s", symbol)

	printTableHeader()

	for {
		// Fetch the BTCUSDT price
		tickerPrice, err := fetchTickerData(priceURL)
		if err != nil {
			fmt.Println("Error fetching price data:", err)
			os.Exit(1)
		}

		// Fetch the BTCUSDT stats
		tickerStats, err := fetchTickerData(statsURL)
		if err != nil {
			fmt.Println("Error fetching stats data:", err)
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

		// Print the current row of data
		fmt.Printf("| %-19s | %-10s | %-15s | %-20s |\n", currentTime, tickerPrice.Symbol, formattedPrice, formattedPriceChangePct)

		time.Sleep(60 * time.Second) // Wait for 60 seconds before refreshing
	}
}
