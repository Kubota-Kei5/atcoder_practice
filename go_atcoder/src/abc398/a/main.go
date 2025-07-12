package main

import (
	"fmt"
	"strings"
)

func main() {

	var n int
	fmt.Scan(&n)

	if n%2 == 0 {
		n -= 1
		fmt.Print(strings.Repeat("-", n/2))
		fmt.Print("==")
		fmt.Print(strings.Repeat("-", n/2))
	} else {
		fmt.Print(strings.Repeat("-", n/2))
		fmt.Print("=")
		fmt.Print(strings.Repeat("-", n/2))
	}
}
