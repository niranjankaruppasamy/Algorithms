package main

import "fmt"

func main() {
loop:
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			if j == 4 {
				break loop
			}
			fmt.Printf("%d%d ", i, j)
		}
		fmt.Println()
	}
}
