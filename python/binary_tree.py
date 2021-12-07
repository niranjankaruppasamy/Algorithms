from typing import Any


class Tree:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, val: Any):
        if self.data is None:
            self.data = Tree(val)
            return
        if val < self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Tree(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Tree(val)

    def inorder(self):
        # inorder order traversal
        elements = list()
        if self.left:
            elements += self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder()
        return elements

    def preorder(self):
        # pre order traversal
        elements = list()
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder()
        if self.right:
            elements += self.right.preorder()
        return elements

    def postorder(self):
        # post order traversal
        elements = list()
        if self.left:
            elements += self.left.postorder()
        if self.right:
            elements += self.right.postorder()
        elements.append(self.data)
        return elements

    def search(self, val: Any):
        if self.data == val:
            return True
        # check left side nodes
        if self.data > val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        # check righ side nodes
        if self.data < val:
            if self.right:
                return self.right.search(val)
            else:
                return False

if __name__ == "__main__":
    tree = Tree(50)
    tree.insert(25)
    tree.insert(30)
    tree.insert(40)
    tree.insert(80)
    tree.insert(90)
    print(tree.inorder())
    print(tree.preorder())
    print(tree.postorder())
    print(tree.search(25))
