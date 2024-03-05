from Laboratory.common_classes.Classes import *
from Laboratory.common_methods.type_list_methods import double_link_list_to_circular_list
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
    initialize: bool = False  # this is the size of the result list

    if isinstance(fx.get_head().get_data(), Term):
        while x is not None:
            xt: Term = x.get_data()
            y = x.get_right_link()
            while y is not None:
                yt: Term = y.get_data()

                # if therms are similar, and the grade had not reduced, and the terms are not the same
                if xt.get_grade() == yt.get_grade() and not checked.contains(yt.get_grade()) and x != y:
                    # then we are going to reduce
                    if not initialize:
                        result = List(sum_term(xt, yt))
                        checked.add(xt.get_grade())
                        initialize = True
                    else:
                        result.add(sum_term(xt, yt))
                        checked.add(xt.get_grade())

                y = y.get_right_link()
            if not checked.contains(xt.get_grade()):
                if not initialize:
                    result = List(xt)
                    initialize = True
                else:
                    result.add(xt)
            x = x.get_right_link()
    else:
        raise RuntimeError("IInvalid Paramaters")

    return result


def resting_terms(n, grades, result) -> List:
    while n is not None:
        nt: Term = n.get_data()
        if not grades.contains(nt.get_grade()):
            result.add(nt)
        n = n.get_right_link()
    return result


def rest_polynomials(px: List, qx: List) -> CList:
    result: List
    grades: List = List(-1)  # this list has the reduced grades
    px = reduce_polynomial(px)
    qx = reduce_polynomial(qx)
    p: Node = px.get_head()
    q: Node = qx.get_head()
    initialize = False
    if isinstance(p.get_data(), Term) and isinstance(q.get_data(), Term):
        while p is not None:
            pt: Term = p.get_data()
            q = qx.get_head()
            while q is not None:
                qt: Term = q.get_data()
                if pt.get_grade() == qt.get_grade():
                    if not initialize:  # this validation check that
                        result = List(rest_term(pt, qt))
                        grades.add(pt.get_grade())
                        initialize = True  # the list result has been initialized
                    else:
                        result.add(rest_term(pt, qt))
                        grades.add(pt.get_grade())
                q = q.get_right_link()
            p = p.get_right_link()
        result = resting_terms(px.get_head(), grades, result)  # this function add the resting terms
        result = resting_terms(qx.get_head(), grades, result)
    else:
        raise RuntimeError("Invalid Parameters")
    return double_link_list_to_circular_list(result)
