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
        if index == 0:
            self.insert_at_beginning(val)
            return
        if index == self.get_length:
            self.insert_at_end(val)
            return
        if index > self.get_length:
            raise IndexError("Invalid index")
        node = self.head.next
        counter = 1
        while node:
            if counter == index - 1:
                node.next = Node(val, node.next)
                return
            node = node.next
            counter += 1

    def printList(self):
        if self.head is None:
            print("Linked list is empty")
        node = self.head
        res = ""
        while node:
            res += str(node.data) + "-->"
            node = node.next
        print(res)

    def delete_from_beginning(self):
        self.head = self.head.next

    def delete_from_end(self):
        curr = self.head
        while curr:
            if curr.next.next is None:
                curr.next = None
                break
            curr = curr.next

    def delete_at_index(self, index: int):
        # delete node based on index
        if index > self.get_length:
            raise IndexError("Invalid Index")
        if index == 0:
            self.delete_from_beginning()
            return
        if index == self.get_length:
            self.delete_from_end()
            return
        counter = 0
        curr = self.head
        while curr:
            if counter == index - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            counter += 1

    def delete_by_value(self, val: Any):
        # delete node based on the value
        curr = self.head
        if curr.data == val:
            self.head = self.head.next
            return
        while curr:
            if curr.next.data == val:
                curr.next = curr.next.next
                break
            curr = curr.next

    def insert_after(self, val_to_add: Any, value_after: Any):
        curr = self.head
        while curr:
            if curr.data == value_after:
                curr.next = Node(val_to_add, curr.next)
                break
            curr = curr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_at(5, 4)
    ll.delete_at_index(2) # will remove 3
    try:
        ll.insert_at(6, 10) # raise IndexError
    except IndexError:
        print("Error!")
    ll.delete_by_value(1)
    ll.insert_after(3, 2)
    ll.printList()
