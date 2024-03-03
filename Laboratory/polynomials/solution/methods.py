from Laboratory.common_classes.Classes import *
from Laboratory.polynomials.solution.term import Term

"""
this document contains the necessary
functions to solves polynomials rest
the solution consist in bind the polynomial 
in an unic list to latter reduce it
"""


def poly_print(slist: List):
    _node = slist.get_head()
    term: Term
    while _node is not None:
        term = _node.get_data()
        print(f"{term.get_coefficient()} X ^ {term.get_grade()}")
        _node = _node.get_right_link()


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
    i: int = 0  # this is the size of the result list

    while x is not None:
        xt: Term = x.get_data()
        y = x.get_right_link()
        while y is not None:
            yt: Term = y.get_data()

            # if therms are similar, and the grade had not reduced, and the terms are not the same
            if xt.get_grade() == yt.get_grade() and not checked.contains(yt.get_grade()) and x != y:
                # then we are going to reduce
                if i == 0:
                    result = List(sum_term(xt, yt))
                    i += 1
                    checked.add(xt.get_grade())
                else:
                    result.add(sum_term(xt, yt))
                    i += 1
                    checked.add(xt.get_grade())

            y = y.get_right_link()

        if not checked.contains(xt.get_grade()):
            if i == 0:
                result = List(xt)
                i += 1
            else:
                result.add(xt)
                i += 1
        x = x.get_right_link()

    checked.print()

    return result


def resting_terms(n, grades, result) -> List:
    while n is not None:
        nt: Term = n.get_data()
        if not grades.contains(nt.get_grade()):
            result.add(nt)
        n = n.get_right_link()
    return result


def rest_polynomials(px: List, qx: List) -> List:
    result: List
    grades: List = List(-1)  # this list has the reduced grades
    px = reduce_polynomial(px)
    qx = reduce_polynomial(qx)

    p: Node = px.get_head()
    q = qx.get_head()
    index = 0
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
                        grades.add(pt.get_grade())
                    else:
                        result.add(rest_term(pt, qt))
                        index += 1
                        grades.add(pt.get_grade())
                q = q.get_right_link()
            p = p.get_right_link()
        result = resting_terms(px.get_head(), grades, result)  # this function add the resting terms
        result = resting_terms(qx.get_head(), grades, result)
    else:
        raise RuntimeError("Invalid Parameters")
    return result
