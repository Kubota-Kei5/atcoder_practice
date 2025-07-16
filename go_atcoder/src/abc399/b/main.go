package main

import (
	"fmt"
)

func solve(a []int, n int) []int {
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		cnt := 1
		for j := 0; j < n; j++ {
			if i == j {
				continue
			}
			if a[i] < a[j] {
				cnt++
			}
		}
		ans[i] = cnt
	}
	return ans
}

func main() {
	var n int
	fmt.Scan(&n)

	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

	ans := solve(a, n)
	for _, v := range ans {
		fmt.Println(v)
	}
}
