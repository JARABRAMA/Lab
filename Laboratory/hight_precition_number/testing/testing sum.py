from Laboratory.common_classes.Classes import List
from Laboratory.hight_precition_number.solution.methods import sum_numbers

a = List(1)
a.add(2)

b = List(1)
b.add(9)

# target  12 + 19 = 31

nsum: List = sum_numbers(a, b)
nsum.print()
