from Laboratory.polynomials.solution.methods import *
from Laboratory.polynomials.solution.term import Term
from Laboratory.common_classes.Classes import *

# creation of px polynomial
p1 = Node(
    Term(
        coefficient=4,
        grade=2
    )
)
px = List(p1)
px.add(
    Term(
        coefficient=-2,
        grade=1
    )
)
px.add(
    Term(
        coefficient=3,
        grade=0
    )
)

# Creation of qx polynomial
q1 = Node(
    Term(
        coefficient=2,
        grade=2
    )
)
qx = List(q1)
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


result = rest_polynomials(px, qx)
poly_print(result)
