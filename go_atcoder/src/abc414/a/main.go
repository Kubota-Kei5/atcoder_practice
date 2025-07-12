package main

import (
	"fmt"
)

func judge(l, r, x, y int) bool {
	if x <= l && r <= y {
		return true
	}
	return false
}
func main() {

	var n, l, r int
	fmt.Scanf("%d %d %d", &n, &l, &r)

	var result int = 0

	for i := 0; i < n; i++ {
		var x, y int
		fmt.Scan(&x, &y)
		if judge(l, r, x, y) {
			result += 1
		}
	}
	fmt.Println(result)
}
