from Laboratory.common_classes.Classes import List, Node
from Laboratory.hight_precition_number.solution.clases import Hp_number
""""
Elabore un algoritmo que sume dos números 
de alta precisión representados como LSL dejando el
resultado en el objeto LSL que invocó el método.
"""


def sum_integer(a: List, b: List, rest: int) -> List:
    if isinstance(a.get_head().get_data(), int) and isinstance(b.get_head().get_data(), int):
        n_sum = 0
        result: List
        initialize: bool = False
        an: Node = a.last()  # node of number a
        bn: Node = b.last()  # node of number b

        while an is not None and bn is not None:
            n_sum = an.get_data() + bn.get_data() + rest
            rest = n_sum // 10
            if not initialize:
                number = n_sum % 10
                result = List(number)
                initialize = True
            else:
                result.insert(0, n_sum % 10)
            an = an.get_left_link()
            bn = bn.get_left_link()

        if an is not None:
            while an is not None:
                n_sum = an.get_data() + rest
                rest = n_sum // 10
                number = n_sum % 10
                result.insert(0, number)
                an = an.get_left_link()
            if rest != 0:
                result.insert(0, rest)

        if bn is not None:
            while bn is not None:
                n_sum = bn.get_data() + rest
                rest = n_sum // 10
                number = n_sum % 10
                result.insert(0, number)
                bn = bn.get_left_link()
            if rest != 0:
                result.insert(0, rest)
        return result

    else:
        raise RuntimeError("Invalid Parameters")


def sum_decimal(a: List, b: List) -> list:
    if isinstance(a.get_head().get_data(), int) and isinstance(b.get_head().get_data(), int):
        rest, n_sum = 0, 0
        result: List
        target = []  # target will contains the result of the sum and the rest
        initialize: bool = False
        an, bn = a.last(), b.last()

        if a.size() > b.size():
            for i in range(a.size() - b.size()):
                if not initialize:
                    result = List(an.get_data())
                    initialize = True
                else:
                    result.insert(0, an.get_data())
                an = an.get_left_link()
        elif b.size() > a.size():
            for i in range(b.size() - a.size()):
                if not initialize:
                    result = List(bn.get_data())
                    initialize = True
                else:
                    result.insert(0, bn.get_data())
                bn = bn.get_left_link()

        while an is not None and bn is not None:
            n_sum = an.get_data() + bn.get_data() + rest
            rest = n_sum // 10
            if not initialize:
                number = n_sum % 10
                result = List(number)
                initialize = True
            else:
                result.insert(0, n_sum % 10)
            an = an.get_left_link()
            bn = bn.get_left_link()

        target = [rest, result]
        return target

def sum_hig_p_number(a: Hp_number, b: Hp_number)->Hp_number:
    decimal_result = sum_decimal(a.decimal, b.decimal)
    return Hp_number(
        decimal= decimal_result[1],
        integer= sum_integer(a.integer, b.integer, decimal_result[0])
    )

def print_hp_number(number: Hp_number):
    number.integer.print()
    print(",")
    number.decimal.print()