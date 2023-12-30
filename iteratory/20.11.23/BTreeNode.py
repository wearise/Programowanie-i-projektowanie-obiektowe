class BTreeNode:
    def __init__(self, val):
        self.val = val
        self.__parent = None
        self.__left = None
        self.__right = None
        # self.flag = 0

    def __str__(self):
        return str(self.val)

    @property
    def left(self): return self.__left

    @left.setter
    def left(self, node: "BTreeNode"):
        self.__left = node
        node.__parent = self

    @property
    def right(self): return self.__right

    @right.setter
    def right(self, node: "BTreeNode"):
        self.__right = node
        node.__parent = self

    @property
    def parent(self): return self.__parent


if __name__ == '__main__':
    root = BTreeNode("1")
    root.left = BTreeNode("2")
    root.right = BTreeNode("3")
    root.left.left = BTreeNode("4")
    root.left.right = BTreeNode("5")

    w = root.right
    print(f"rodzicem {w} jest {w.parent}")
