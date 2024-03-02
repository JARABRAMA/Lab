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

    def last(self) -> Node:
        e_node = self._node
        while e_node.get_right_link() is not None:
            e_node = e_node.get_right_link()
        return e_node

    def __add__(self, data):
        other = Node(data)

        other._left_link = self.last()
        self.last()._right_link = other

    def __getitem__(self, index: int) -> Node:
        e_node = self._node
        for i in range(index):
            e_node = e_node.get_right_link()

        return e_node

    def insert(self, index: int, data):
        new_node: Node = Node(data)
        _node: Node = self.__getitem__(index - 2)  # the anterior position that i what to insert

        if _node.get_right_link() is None:
            self.__add__(data)
        else:
            new_node.set_left_link(_node)
            new_node.set_right_link(_node.get_right_link())
            _node.get_right_link().set_left_link(new_node)
            _node.set_right_link(new_node)

    def print(self):
        e_node = self._node
        while e_node is not None:
            print(f"Node__{e_node.get_data()}")
            e_node = e_node.get_right_link()


class CList:
    def __init__(self, node: Node):
        self._node = node
