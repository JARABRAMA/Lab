class Node:

    def __init__(self, data):
        self._data = data
        self._left_link = None
        self._right_link = None

    def set_right_link(self, link):
        self._right_link = link

    def get_right_link(self):
        return self._right_link

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_left_link(self, link):
        self._left_link = link

    def get_left_link(self):
        return self._left_link


class List:  # Double link list
    def __init__(self, node: Node):
        self._node = node

    def get_head(self) -> Node:
        return self._node

    def last(self) -> Node:
        e_node = self._node
        while e_node.get_right_link() is not None:
            e_node = e_node.get_right_link()
        return e_node

    def add(self, data):
        other: Node = Node(data)

        other.set_left_link(self.last())
        self.last().set_right_link(other)

    def getitem(self, index: int) -> Node:
        e_node = self._node
        for i in range(index):
            e_node = e_node.get_right_link()

        return e_node

    def insert(self, index: int, data):
        new_node: Node = Node(data)
        _node: Node = self.getitem(index - 2)  # the previous position that i what to insert

        if _node.get_right_link is None:
            self.add(data)
        else:
            new_node.set_left_link(_node)
            new_node.set_right_link(_node.get_right_link)
            _node.get_right_link().set_left_link(new_node)
            _node.set_right_link(new_node)

    def print(self):
        e_node = self._node
        while e_node is not None:
            print(f"Node__{e_node.get_data()}")
            e_node = e_node.get_right_link


class CList:  # Circular List
    def __init__(self, node: Node):
        self._node = node
        self._node.set_right_link(node)
        self._node.set_left_link(node)

    def get_head(self) -> Node:
        return self._node

    def add(self, data):
        other: Node = Node(data)

        other.set_right_link(self._node)
        other.set_left_link(self.last())
        self.last().set_right_link(other)
        self._node.set_left_link(other)

    def last(self) -> Node:
        node: Node = self._node.get_right_link()

        while node.get_right_link() != self._node:
            node = node.get_right_link()

        return node

    def print(self):
        print(f"data: __{self._node.get_data()}")
        node: Node = self._node.get_right_link()
        while node != self._node:
            print(f"data: __{node.get_data()}")
            node = node.get_right_link()

    def item(self, index: int) -> Node:
        node: Node = self._node
        for i in range(index):
            node = node.get_right_link()
            if node == self._node:
                raise RuntimeError("Invalid Index")
        return node

    def insert(self, index: int, data):
        other: Node = Node(data)
        previous: Node = self.item(index).get_left_link()

        if previous.get_right_link() is None:
            self.add(data)
        else:
            other.set_left_link(previous)
            other.set_right_link(previous.get_right_link())
            previous.get_right_link().set_left_link(other)
            previous.set_right_link(other)
