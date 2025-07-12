package main

import (
	"fmt"
)

func judge(values []int) bool {
	for i := 0; i < len(values)-2; i++ {
		if values[i] == values[i+1] && values[i+1] == values[i+2] {
			return true
		}
	}
	return false
}

func main() {

	var n int
	fmt.Scan(&n)
	values := make([]int, n)

	for i := 0; i < n; i++ {
		var a int
		fmt.Scan(&a)
		values[i] = a
	}

	if judge(values) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
