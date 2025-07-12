package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)

	var length int64
	result := make([]string, 0)
	tooLong := false

	for i := 0; i < n; i++ {
		var c string
		var l int64
		fmt.Scanf("%s %d", &c, &l)

		length += l
		if length > 100 {
			tooLong = true
		}

		if !tooLong {
			for j := int64(0); j < l; j++ {
				result = append(result, c)
			}
		}
	}

	if tooLong {
		fmt.Println("Too Long")
	} else {
		fmt.Println(strings.Join(result, ""))
	}
}
