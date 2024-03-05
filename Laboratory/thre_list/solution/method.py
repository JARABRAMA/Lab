from Laboratory.common_classes.Classes import List, Node


def common_elements(a: List, b: List, c: List) -> List:
    solution: List = List("string")
    init = False
    an = a.get_head()
    bn: Node = b.get_head()
    cn: Node = c.get_head()

    init = False
    while an is not None:
        while bn is not None:

            if an.get_data() == bn.get_data():
                while cn is not None:
                    if cn.get_data() == an.get_data():
                        if not init:
                            solution = List(an.get_data())
                            init = True
                        else:
                            solution.add(an.get_data())
                    cn = cn.get_right_link()

            bn = bn.get_right_link()
        an = an.get_right_link()  # Ultima instruccion
    return solution