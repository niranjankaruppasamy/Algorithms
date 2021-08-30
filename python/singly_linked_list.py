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
    ll.print()
