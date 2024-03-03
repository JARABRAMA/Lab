from Laboratory.common_classes.Classes import *
from Laboratory.polynomials.solution.term import Term

"""
this document contains the necessary
functions to solves polynomials rest
the solution consist in bind the polynomial 
in an unic list to latter reduce it
"""


def rest_term(term_p: Term, term_q: Term) -> Term:
    # is a fact that the terms are similar
    return Term(
        coefficient=term_p.get_coefficient() - term_q.get_coefficient(),
        grade=term_q.get_grade()
    )


def bind_polynomials(px: List, qx: List) -> List:
    result: List = List(px.get_head())
    qx.get_head().set_left_link(result.last())
    result.last().set_right_link(qx.get_head())

    # while _node is not None:
    #    result.add(_node.get_data())
    #   _node = _node.get_right_link()

    return result


def reduce_polynomial(fx: List) -> List:
    x: Term
    y: Term
    result: List
    index = 0

    sump: bool = False
    n1: Node = fx.get_head()
    while n1 is not None:
        n2: Node = n1.get_right_link()

        while n2 is not None:
            if n1.get_data().get_grade() == n2.get_data().get_grade() and n1 != n2:
                if index == 0:
                    result = List(
                        Node(
                            rest_term(n1.get_data(), n2.get_data())
                        )
                    )
                    index += 1
                else:
                    result.add(
                        rest_term(n1.get_data(), n2.get_data())
                    )
                    index += 1
            n2 = n2.get_right_link()

        n1 = n1.get_right_link()
    return result
