from Laboratory.common_classes.Classes import List, Node

""""
Elabore un algoritmo que sume dos números 
de alta precisión representados como LSL dejando el
resultado en el objeto LSL que invocó el método.
"""


def sum_numbers(a: List, b: List) -> List:
    if isinstance(a.get_head().get_data(), int) and isinstance(b.get_head().get_data(), int):
        rest, n_sum = 0, 0
        result: List
        initialize: bool = False
        an: Node = a.last()  # node of number a
        bn: Node = b.last()  # node of number b

        # when the numbers have the same length
        if a.size() == b.size():
            while an is not None and bn is not None:
                n_sum = an.get_data() + bn.get_data() + rest
                rest = n_sum // 10
                if not initialize:
                    result = List(n_sum % 10)
                else:
                    result.insert(0, n_sum % 10)
                an = an.get_right_link()
                bn = bn.get_right_link()
            result.insert(0, rest)
            return result
    else:
        raise RuntimeError("Invalid Parameters")
