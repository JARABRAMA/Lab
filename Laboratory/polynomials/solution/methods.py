from Laboratory.common_classes.Classes import *
from Laboratory.polynomials.solution.term import Term

"""
this document contains the necessary
functions to solves polynomials rest
the solution consist in bind the polynomial 
in an unic list to latter reduce it
"""


def sum_term(term_p: Term, term_q: Term) -> Term:
    # is a fact that the terms are similar
    return Term(
        coefficient=term_p.get_coefficient() + term_q.get_coefficient(),
        grade=term_q.get_grade()
    )


def rest_term(term_p: Term, term_q: Term) -> Term:
    # is a fact that the terms are similar
    return Term(
        coefficient=term_p.get_coefficient() - term_q.get_coefficient(),
        grade=term_q.get_grade()
    )


def rest_polynomials(px: List, qx: List) -> List:
    result: List
    p: Node = px.get_head()
    q = qx.get_head()
    index = 0
    sum_check: bool = False
    if isinstance(p.get_data(), Term) and isinstance(q.get_data(), Term):

        while p is not None:
            pt: Term = p.get_data()
            q = qx.get_head()

            while q is not None:
                qt: Term = q.get_data()

                if pt.get_grade() == qt.get_grade():  # this validation check that
                    if index == 0:  # the list result has been initialized
                        result = List(
                            Node(rest_term(pt, qt))
                        )
                        index += 1
                        sum_check = True
                    else:
                        result.add(rest_term(pt, qt))
                        sum_check = True
                        index += 1

                q = q.get_right_link()

            if not sum_check:
                if index == 0:
                    result = List(p)
                    sum_check = False
                    index += 1
                else:
                    result.add(
                        p.get_data()
                    )
                    index += 1
                    sum_check = False

            p = p.get_right_link()

    else:
        raise RuntimeError("Invalid Parameters")

    return result
