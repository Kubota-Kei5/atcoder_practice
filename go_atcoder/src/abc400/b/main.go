package main

import (
	"fmt"
	"math"
)

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func main() {
	var n, m int
	fmt.Scanf("%d %d", &n, &m)

	var ans int = 0
	for i := 0; i < m+1; i++ {
		ans += pow(n, i)
		if ans > 1000000000 {
			ans = -1
			break
		}
	}

	if ans > -1 {
		fmt.Println(ans)
	} else {
		fmt.Println("inf")
	}
}
