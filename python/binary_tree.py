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

    def print_tree(self):
        # pre order traversal
        print(self.data)

        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()


if __name__ == "__main__":
    tree = Tree(50)
    tree.insert(25)
    tree.insert(30)
    tree.insert(40)
    tree.insert(80)
    tree.print_tree()
