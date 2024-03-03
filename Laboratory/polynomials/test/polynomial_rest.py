from Laboratory.polynomials.solution.methods import *
from Laboratory.polynomials.solution.term import Term
from Laboratory.common_classes.Classes import *

px = List(
    Term(
        coefficient=4,
        grade=2
    )
)
px.add(
    Term(
        coefficient=-2,
        grade=2
    )
)
px.add(
    Term(
        coefficient=3,
        grade=0
    )
)

# Creation of qx polynomial
qx = List(
    Term(
        coefficient=2,
        grade=2
    )
)
qx.add(
    Term(
        coefficient=8,
        grade=1
    )
)
qx.add(
    Term(
        coefficient=2,
        grade=0
    )
)


def poly_print(slist: List):
    _node = slist.get_head()
    term: Term
    while _node is not None:
        term = _node.get_data()
        print(f"{term.get_coefficient()} X ^ {term.get_grade()}")
        _node = _node.get_right_link()


result = reduce_polynomial(px)
poly_print(result)
