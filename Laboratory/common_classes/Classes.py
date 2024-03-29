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
    def __init__(self, data):
        self._node = Node(data)

    def size(self) -> int:
        index = 0
        _node: Node = self.get_head()
        while _node is not None:
            _node = _node.get_right_link()
            index += 1
        return index

    def get_head(self) -> Node:
        return self._node

    def set_head(self, node: Node):
        self._node = node

    def last(self) -> Node:
        e_node = self._node
        while e_node.get_right_link() is not None:
            e_node = e_node.get_right_link()
        return e_node

    def contains(self, item) -> bool:
        node: Node = self.get_head()
        contains: bool = False
        while node is not None:
            if node.get_data() == item:
                contains = True
                break
            node = node.get_right_link()
        return contains

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
        if index != 0:
            _node: Node = self.getitem(index - 2)  # the previous position that i what to insert

            if _node.get_right_link is None:
                self.add(data)
            else:
                new_node.set_left_link(_node)
                new_node.set_right_link(_node.get_right_link)
                _node.get_right_link().set_left_link(new_node)
                _node.set_right_link(new_node)
        else:
            self.get_head().set_left_link(new_node)
            new_node.set_right_link(self.get_head())
            self.set_head(new_node)

    def print(self):
        e_node = self._node
        while e_node is not None:
            print(f"Node__{e_node.get_data()}")
            e_node = e_node.get_right_link()


class CList:  # Circular List
    def __init__(self, data):
        self._node = Node(data)
        self._node.set_right_link(self._node)
        self._node.set_left_link(self._node)
        self._size = 1

    def get_head(self) -> Node:
        return self._node

    def size(self) -> int:
        return self._size

    def increase_size(self):
        self._size += 1

    def add(self, data):
        self.increase_size()
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
        self.increase_size()

        other: Node = Node(data)
        previous: Node = self.item(index).get_left_link()

        if previous.get_right_link() is None:
            self.add(data)
        else:
            other.set_left_link(previous)
            other.set_right_link(previous.get_right_link())
            previous.get_right_link().set_left_link(other)
            previous.set_right_link(other)
