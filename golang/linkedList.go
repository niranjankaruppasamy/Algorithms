package main

import (
	"fmt"
	"strconv"
)

type Node struct {
	data int
	next *Node
}

type linkedList struct {
	head *Node
}

func (l *linkedList) InsertAtBeginning(val int) {
	if l.head == nil {
		l.head = &Node{val, nil}
	} else {
		node := &Node{val, l.head}
		l.head = node
	}
}

func (l *linkedList) InsertAtEnd(val int) {
	if l.head == nil {
		l.head = &Node{val, nil}
	} else {
		curr := l.head
		for {
			if curr.next == nil {
				curr.next = &Node{val, nil}
				return
			}
			curr = curr.next
		}
	}
}

func (l *linkedList) Print() {
	if l.head == nil {
		fmt.Println("Linked list is empty")
	}
	node := *l.head
	var res string = ""
	for {
		res = res + strconv.Itoa(node.data) + "-->"
		if node.next == nil {
			break
		}
		node = *node.next
	}
	fmt.Println(res)
}

func main() {
	var ll = linkedList{}
	ll.InsertAtBeginning(30)
	ll.InsertAtBeginning(20)
	ll.InsertAtBeginning(10)
	ll.InsertAtEnd(40)
	ll.Print()
}
