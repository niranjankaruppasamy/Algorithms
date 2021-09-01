package main

import "fmt"


type Node struct {
	data int
	next *Node
}

type linkedList struct {
	head *Node
	len  int
}

func (l *linkedList) insert(val int) {
	node := Node{}
	node.data = val
	if l.len == 0 {
		l.head = &node
		l.len++
		return
	}
	ptr := l.head
	for i := 0; i < l.len; i++ {
		if ptr.next == nil {
			ptr.next = &node
			l.len++
			return
		}
		ptr = ptr.next
	}
}

func (l *linkedList) print() {
	if l.len == 0 {
		fmt.Println("No nodes")
	} else {
		current := l.head
		for i := 0; i < l.len; i++ {
			fmt.Println(current.data)
			current = current.next
		}
	}
}

func main() {
	var ll = linkedList{nil, 0}
	ll.insert(1)
	ll.insert(2)
	ll.print()
	fmt.Println(ll.len)
}
