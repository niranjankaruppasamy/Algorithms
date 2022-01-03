
class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, data):
        data.parent = self
        self.child.append(data)

    def get_level(self):
        counter = 0
        while self.parent:
            counter += 1
            self = self.parent
        return counter

    def print_data(self):
        prefix = " " * self.get_level() * 3 + "___|"
        print(prefix + self.data)
        for child in self.child:
            child.print_data()

if __name__ == "__main__":
    t = Tree("Electronics")

    e1 = Tree("TV")

    e1.add_child(Tree("Philips"))
    e1.add_child(Tree("Sony"))
    e1.add_child(Tree("Samsung"))


    e2 = Tree("Computer")

    e2.add_child(Tree("HP"))
    e2.add_child(Tree("Dell"))
    e2.add_child(Tree("Lenovo"))


    e3 = Tree("Mobile")

    e3.add_child(Tree("Apple"))
    e3.add_child(Tree("Samsung"))
    e3.add_child(Tree("Oneplus"))

    t.add_child(e1)
    t.add_child(e2)
    t.add_child(e3)

    t.print_data()

