from Laboratory.common_classes.Classes import *


def create_list() -> List:
    stop: bool = False
    index = 0
    data: int = int(input(f"Enter the data of the index {index}: __"))
    nodal_list = List(data)

    while not stop:
        index += 1
        try:
            data: int = int(input(f"Enter the data of the index {index}: __"))
            nodal_list.add(data)
        except ValueError:
            stop = True

    return nodal_list


nlist = create_list()
nlist.print()
print("##########")
nlist.insert(0, -1)
nlist.print()
print("##########")
nlist.insert(0, -2)
nlist.print()
print("##########")
