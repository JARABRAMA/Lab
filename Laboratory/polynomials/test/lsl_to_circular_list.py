from Laboratory.common_classes.Classes import List, CList, Node
from Laboratory.polynomials.solution.methods import double_link_list_to_circular_list

lsl = List(0)
lsl.add(2)
lsl.add(3)
lsl.add(4)
lsl.add(5)

circular = double_link_list_to_circular_list(lsl)
circular.print()
