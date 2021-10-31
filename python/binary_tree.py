from typing import Any


class Node:
    def __init__(self, data: Any, left: Any = None, right: Any = None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val: Any):
        if self.root is None:
            self.root = Node(val)
            return
