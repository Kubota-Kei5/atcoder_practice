package main

import (
	"fmt"
)

func main() {
	var n, result int
	var s, t string
	fmt.Scan(&n, &s, &t)

	for i := 0; i < n; i++ {
		if s[i] != t[i] {
			result++
		}
	}
	fmt.Println(result)
}
