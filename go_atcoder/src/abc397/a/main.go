package main

import (
	"fmt"
)

func main() {
	var n float64
	fmt.Scan(&n)

	if n >= 38 {
		fmt.Println(1)
	} else if n < 37.5 {
		fmt.Println(3)
	} else {
		fmt.Println(2)
	}
}
