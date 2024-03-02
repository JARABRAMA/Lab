from Laboratory.common_classes.Classes import *


def circular_list() -> CList:
    node: Node
    index = 0
    stop = False
    data = int(input(f"enter the data of {index} index: __"))
    node = Node(data)
    c_list = CList(node)
    while not stop:
        try:
            index += 1
            data = int(input(f"enter the data of {index} index: __"))
            c_list.add(data)
        except ValueError:
            stop = True
    return c_list


clist = circular_list()
clist.print()

clist.insert(2, 90)
print("###########################")
clist.print()
