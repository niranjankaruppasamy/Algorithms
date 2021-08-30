from typing import Any


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val: Any):
        node = Node(val, self.head)
        self.head = node

    def insert_at_end(self, val:Any):
        node = self.head
        while node:
            if node.next is None:
                node.next = Node(val, None)
                break
            node = node.next

    @property
    def get_length(self) -> int:
        counter = 0
        node = self.head
        while node:
            node = node.next
            counter += 1
        return counter

    def insert_at(self, val: Any, index: int):
        ...

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        node = self.head
        res = ""
        while node:
            res += str(node.data) + "-->"
            node = node.next
        print(res)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(10)
    ll.insert_at_end(5)
    ll.insert_at_end(65)
    ll.print()
    print(ll.get_length)
