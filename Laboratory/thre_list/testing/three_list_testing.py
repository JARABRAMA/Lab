from Laboratory.common_classes.Classes import List
from Laboratory.thre_list.solution.method import common_elements

a = List(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)

b = List(2)
b.add(4)
b.add(5)
b.add(6)
b.add(7)

c = List(4)
c.add(5)
c.add(6)
c.add(7)
c.add(8)

# caso de prueba
# {1, 2, 3, 4, 5}
# {2, 4, 5, 6, 7}
# {4, 5, 6, 7, 8}

# target = {4, 5}
target = common_elements(a, b, c)
target.print()
