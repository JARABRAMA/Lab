"""
this document contains the necessary
functions to solves multiplication of polynomials
"""
from Laboratory.common_classes.Classes import *
from Laboratory.polynomials.term import Term


def sum_polynomial(p1: List, p2: List) -> CList:
    if p1.getitem(0).get_data() is Term and p2.getitem(0).get_data() is Term:
        # is a fact that the polynomial is sort

