package main

import "fmt"

func AddElementstoMap(mapper map[int]int, array []int) map[int]int {
	for index := range array {
		mapper[index] = array[index]
	}
	return mapper
}

func main() {
	var mapper = map[int]int{}
	var array []int = []int{9, 8, 7, 6, 5}

	// adding element
	AddElementstoMap(mapper, array)
	fmt.Println(mapper)

	// access element
	val, exist := mapper[7]
	fmt.Println(val, exist)

	// delete element key based
	delete(mapper, 0)
	fmt.Println(mapper)
}
