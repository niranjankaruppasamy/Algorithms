package main

import (
	"fmt"
)

func linearSearch(arr []int, searchValue int) int {
	for index, value := range arr {
		if value == searchValue {
			return index
		}
	}
	return 0
}

func main() {
	var arr = []int{67, 7, 23, 756, 2343, 6754, 233, 5645, 1, 4, 65, 90}
	searchValue := 4
	index := linearSearch(arr, searchValue)
	fmt.Println(index)
}
