from Laboratory.polynomials.solution.methods import *
from Laboratory.polynomials.solution.term import Term
from Laboratory.common_classes.Classes import *

px = List(
    Term(
        coefficient=1,
        grade=2
    )
)
px.add(
    Term(
        coefficient=1,
        grade=2
    )
)
px.add(
    Term(
        coefficient=8,
        grade=0
    )
)

# Creation of qx polynomial
qx = List(
    Term(
        coefficient=1,
        grade=4
    )
)
qx.add(
    Term(
        coefficient=-1,
        grade=3
    )
)
qx.add(
    Term(
        coefficient=1,
        grade=2
    )
)


result = rest_polynomials(px,qx)
print("result")
poly_print(result)
