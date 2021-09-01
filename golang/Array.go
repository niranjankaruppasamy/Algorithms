package main

import "fmt"

func remove(arr []int, index int) []int {
	return append(arr[:index], arr[index+1:]...)
}


func main() {
	var staticArr [5]int = [5]int{1, 2, 3, 4, 5}
	fmt.Println(staticArr)

	var dynamicArr []int = []int{0, 9, 8, 7}
	arr := []int {9, 8, 7}

	// insertion
	dynamicArr = append(dynamicArr, arr...)
	fmt.Println(dynamicArr)

	// remove element from array
	result := remove(dynamicArr, 2)
	fmt.Println(result)
}
