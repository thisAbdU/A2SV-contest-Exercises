package main

import (
	"fmt"
	"time"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n <= 3 {
		return true
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}
	for i := 5; i*i <= n; i += 6 {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
	}
	return true
}

func findPrimes(limit int) {
	for num := 2; num <= limit; num++ {
		isPrime(num)
	}
}

func main() {
	limit := 100000 // Adjust this limit as needed
	start := time.Now()
	findPrimes(limit)
	elapsed := time.Since(start)
	fmt.Printf("Execution Time in Go: %v seconds\n", elapsed.Seconds())
}
