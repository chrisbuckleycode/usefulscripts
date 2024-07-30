// Conduct an internet connectivity test and display statistics
// calculated from the samples gathered, specifically speed in kilobytes per second
// Note: "test" is a reserved goland term in filenames. Hence, in our case we have elected to truncate to "tst"
//
// Instructions:
// go mod init example.com/connectivity-tst
// go mod tidy
// go run connectivity_tst.go

package main

import (
	"fmt"
	"io"
	"math"
	"net/http"
	"sort"
	"strings"
	"time"
)

const (
	samples = 10                                          // Number of samples to take
	url     = "https://hk1.newmediaexpress.com/10MB.test" // URL to download from
)

func main() {
	speeds := make([]float64, samples) // Slice to store download speeds

	// Conduct the test and calculate the statistics
	for i := 0; i < samples; i++ {
		start := time.Now()        // Start time of download
		resp, err := http.Get(url) // Send GET request
		if err != nil {
			fmt.Println("Error:", err) // Print error if any
			return
		}
		defer resp.Body.Close() // Close the response body

		// Create a progress bar
		progress := make(chan float64)
		go func() {
			var totalRead int64
			for p := range progress {
				totalRead += int64(p)
				fmt.Printf("\r%s %.1f%%", strings.Repeat("#", int(totalRead*74/resp.ContentLength)), float64(totalRead)*100/float64(resp.ContentLength))
			}
			fmt.Println()
		}()

		// Discard the response body and report progress
		_, err = io.Copy(io.Discard, &progressReader{resp.Body, progress})
		close(progress)
		if err != nil {
			fmt.Println("Error:", err) // Print error if any
			return
		}
		duration := time.Since(start).Seconds()                   // Calculate download duration
		speeds[i] = float64(resp.ContentLength) / duration / 1024 // Calculate download speed
	}

	sort.Float64s(speeds) // Sort the download speeds
	sum := 0.0
	for _, speed := range speeds {
		sum += speed // Calculate the sum of speeds
	}
	mean := sum / float64(samples) // Calculate mean speed

	varianceSum := 0.0
	for _, speed := range speeds {
		difference := speed - mean
		varianceSum += difference * difference // Calculate the sum of squared differences from the mean
	}
	stdev := math.Sqrt(varianceSum / float64(samples)) // Calculate standard deviation

	// Print the statistics
	fmt.Println()
	fmt.Printf("min: %.2f KB/s\n", speeds[0])
	fmt.Printf("max: %.2f KB/s\n", speeds[samples-1])
	fmt.Printf("mean: %.2f KB/s\n", mean)
	fmt.Printf("stdev: %.2f KB/s\n", stdev)
}

type progressReader struct {
	r io.Reader
	p chan<- float64
}

func (pr *progressReader) Read(p []byte) (n int, err error) {
	n, err = pr.r.Read(p)
	pr.p <- float64(n)
	return
}
