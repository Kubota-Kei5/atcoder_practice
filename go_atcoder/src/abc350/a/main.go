package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	fmt.Scan(&s)

	n := s[3:]
	i, _ := strconv.Atoi(n)

	r := "Yes"
	if i == 0 || i == 316 {
		r = "No"
	}
	if i > 349 {
		r = "No"
	}
	fmt.Println(r)
}
