from Laboratory.common_classes.Classes import List
from Laboratory.hight_precition_number.solution.clases import Hp_number
from Laboratory.hight_precition_number.solution.methods import sum_hig_p_number, print_hp_number

ainteger = List(1)
ainteger.add(2)
ainteger.add(9)

adecimal = List(1)
adecimal.add(2)

a = Hp_number(
    integer=ainteger,
    decimal=adecimal
)
# a = 129,12
binteger = List(1)
binteger.add(3)

bdecimal = List(1)
bdecimal.add(7)
bdecimal.add(3)

b = Hp_number(
    integer=binteger,
    decimal=bdecimal
)
# 13,173

# 129,12 + 13,173

# target = 142,293
target = sum_hig_p_number(a, b)
print_hp_number(target)
