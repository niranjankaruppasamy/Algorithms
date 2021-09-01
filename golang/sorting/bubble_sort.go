package main

import "fmt"

func Swap(a, b int) (int, int) {
	return b, a
}

func BubbleSort(arr []int, size int) []int {
	for i := 0; i < size; i++ {
		for j := 0; j < size-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = Swap(arr[j], arr[j+1])
			}
		}
	}
	return arr
}

func main() {
	var arr []int = []int{98, 4, 2, 7, 5, 10, 33, 1}
	arr = BubbleSort(arr, len(arr))
	fmt.Println(arr)
}
