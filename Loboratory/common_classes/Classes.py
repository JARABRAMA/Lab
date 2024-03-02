class Node:
    def __init__(self, data):
        self.data = data
        self.left_link = None
        self.right_link = None


class List:  # Double link list
    def __init__(self, node: Node):
        self._node = node

    def last(self) -> Node:
        e_node = self._node
        while e_node.right_link is not None:
            e_node = e_node.right_link
        return e_node

    def __add__(self, other: Node):
        other.left_link = self.last()
        self.last().right_link = other

    def __getitem__(self, index: int) -> Node:
        e_node = self._node
        for i in range(index):
            e_node = e_node.right_link

        return e_node

    def insert(self, index: int, data):
        new_node = Node(data)
        e_node = self.__getitem__(index)

    def print(self):
        e_node = self._node
        while e_node is not None:
            print(f"Node__{e_node.data}")
            e_node = e_node.right_link
 
 class CList: 
    def __init__(self, node: Node): 
        self._node = node