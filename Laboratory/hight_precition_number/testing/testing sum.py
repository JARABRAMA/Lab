from Laboratory.common_classes.Classes import List
from Laboratory.hight_precition_number.solution.methods import sum_numbers

a = List(1)
a.add(5)  # 15

b = List(8)
b.add(6)  # 76

# target 15 + 76 = 91

nsum = sum_numbers(a, b)
nsum.print()
