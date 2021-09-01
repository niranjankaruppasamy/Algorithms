package main

import "fmt"

type Name interface {
	getName() string
}

type Person1 struct {
	name string
	age  int
}

type Person2 struct {
	name string
	age  int
}

func (p1 *Person1) getName() string {
	return p1.name
}

func (p2 *Person2) getName() string {
	return p2.name
}

func getFunc(n Name) {
	fmt.Println(n)
}

func main() {
	obj1 := Person1{name: "niranjan", age: 10}
	obj2 := Person2{"chandru", 20}
	fmt.Println(obj1)
	fmt.Println(obj2)
	arr := make([]byte, 5)
	fmt.Println(arr)
	// fmt.Println(obj1.getName())
	// fmt.Println(obj2.getName())
	// getFunc(obj1)
}
