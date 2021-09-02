package main

import (
	"fmt"
)

func binarySearch(arr []int, searchValue int, start int, end int) int {
	if end >= start {
		midPoint := start + (end-start)/2.0
		if arr[midPoint] == searchValue {
			return midPoint
		} else if arr[midPoint] > searchValue {
			return binarySearch(arr, searchValue, start, midPoint-1)
		} else {
			return binarySearch(arr, searchValue, midPoint+1, end)
		}
	}
	return -1
}

func main() {
	arr := []int{1, 4, 7, 45, 78, 89, 123, 655, 877, 1212, 6767}
	searchValue := 878
	var value int = binarySearch(arr, searchValue, 0, len(arr)-1)
	fmt.Println((value))
}
