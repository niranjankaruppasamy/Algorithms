class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, newnode):
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.len += 1

    def prepend(self, newnode):
        newnode.next = self.head
        self.head = newnode
        self.len += 1

    def insert(self, newnode, index):
        if index == 0:
            self.prepend(newnode)
            return
        current_node = self.head
        for i in range(1, self.len):
            if i == index:
                newnode.next = current_node.next
                current_node.next = newnode
                break
            current_node = current_node.next
    
    def deleteNode(self, index):
        pass

    def printList(self):
        current_node = self.head
        for _ in range(self.len):
            print(current_node.data)
            current_node = current_node.next


node0 = Node("blah")
node1 = Node("1st node")
node2 = Node("2nd node")
node3 = Node("3rd node")
node4 = Node("4th node")
node5 = Node("5th node")
linkedlist = LinkedList()

linkedlist.append(node1)
linkedlist.append(node2)
linkedlist.append(node3)
linkedlist.append(node4)
linkedlist.prepend(node0)
linkedlist.insert(node5, 0)
linkedlist.printList()