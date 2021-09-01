package main

import "fmt"

func Reverse(name string) string {
	var arr []byte = []byte{}
	for i := len(name) - 1; i >= 0; i-- {
		arr = append(arr, name[i])
	}
	name = string(arr)
	return name
}

func main() {
	var str string = "Niranjan"
	reversed_str := Reverse(str)
	fmt.Println(reversed_str)
}
