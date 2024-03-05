from Laboratory.common_classes.Classes import List, Node


def common_elements(a: List, b: List, c: List) -> List:
    init = False

    an: Node = a.get_head()
    while an is not None:
        bn = b.get_head()
        while bn is not None:
            if an.get_data() == bn.get_data():
                cn: Node = c.get_head()
                while cn is not None:
                    if cn.get_data() == an.get_data():
                        if not init:
                            solution = List(an.get_data())
                            init = True
                        else:
                            solution.add(an.get_data())
                    cn = cn.get_right_link()
            bn = bn.get_right_link()
        an = an.get_right_link()  # Last instruction

    return solution
