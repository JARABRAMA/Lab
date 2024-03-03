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


def reduce_polynomial(fx: List) -> List:
    result: List
    checked = List(-1)

    x: Node
    y: Node
    term_sum: Term

    x = fx.get_head()
    y = fx.get_head().get_right_link()
    reduce: bool = False
    i: int = 0  # this is the size of the result list

    xt: Term = x.get_data()
    while x is not None:
        xt: Term = x.get_data()
        while y is not None:
            yt: Term = y.get_data()

            if xt.get_grade() == yt.get_grade() and not checked.contains(xt.get_grade()):
                if i == 0:
                    result = List(sum_term(xt, yt))
                    i += 1
                    reduce = True
                    checked.add(xt.get_grade())
                else:
                    result.add(sum_term(xt, yt))
                    i += 1
                    reduce = True
                    checked.add(xt.get_grade())

            y = y.get_right_link()

        if not reduce:
            if i == 0:
                result = List(xt)
                reduce = False
                i += 1
            else:
                result.add(xt)
                reduce = False
                i += 1
        x = x.get_right_link()
    return result


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

                if pt.get_grade() == qt.get_grade():
                    if index == 0:  # this validation check that
                        result = List(  # the list result has been initialized
                            rest_term(pt, qt)
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
                    result = List(pt)
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
