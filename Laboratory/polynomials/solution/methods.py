"""
this document contains the necessary
functions to solves multiplication of polynomials
these methods takes as a fact that the polynomials are order
"""
from Laboratory.common_classes.Classes import *
from Laboratory.polynomials.solution.term import Term


def mayor_grade(px: List, qx: List) -> List:  # this method verifies what polynomial has the mayor grade
    if qx.get_head().get_data() is Term and px.get_head().get_data() is Term:
        px_term: Term = px.get_head().get_data()
        qx_term: Term = qx.get_head().get_data()

        if px_term.get_grade() > qx_term.get_grade():
            return px
        elif px_term.get_grade() < qx_term.get_grade():
            return qx
        else:
            return px
    else:
        raise RuntimeError("Invalid parameters")


def minor_grade(px, qx) -> List:  # this method verifies what polynomial has the minor grade
    if qx.get_head().get_data() is Term and px.get_head().get_data() is Term:
        px_term: Term = px.get_head().get_data()
        qx_term: Term = qx.get_head().get_data()

        if px_term.get_grade() > qx_term.get_grade():
            return qx
        elif px_term.get_grade() < qx_term.get_grade():
            return px
        else:
            return px
    else:
        raise RuntimeError("Invalid parameters")


def sum_term(node_1: Node, node_2: Node) -> Node:
    term1: Term = node_1.get_data()
    term2: Term = node_2.get_data()
    if term1 is Term and term2 is Term:
        if term1.get_grade() == term2.get_grade():
            return Node(
                Term(
                    coefficient=term1.get_coefficient() + term2.get_coefficient(),
                    grade=term2.get_grade()
                )
            )
        else:
            if term1.get_grade() > term2.get_grade():
                return node_1
            else:
                return node_2
    else:
        raise RuntimeError("Invalid Parameters")


def insert_rest(node: Node, c_list: CList) -> CList:
    while node is not None:
        c_list.add(node)
        node = node.get_right_link()


def sum_polynomial(px: List, qx: List) -> CList:
    if px.getitem(0).get_data() is Term and qx.getitem(0).get_data() is Term:
        # Check that the  lists have polynomials

        poly_sum: CList
        node_sum: Node

        mayor_polynomial: List = mayor_grade(px, qx)
        minor_polynomial: List = minor_grade(px, qx)

        node_1: Node = mayor_polynomial.get_head()
        node_2: Node = minor_polynomial.get_head()

        poly_sum = CList(
            sum_term(node_1, node_2)
        )

        node_1 = node_1.get_right_link()
        node_2 = node_2.get_right_link()
        while node_1 is not None and node_2 is not None:
            poly_sum = CList(
                sum_term(node_1, node_2)
            )
            node_1 = node_1.get_right_link()
            node_2 = node_2.get_right_link()
        if node_1 is not None:
            poly_sum = insert_rest(node_1, poly_sum)
        elif node_2 is not None:
            poly_sum = insert_rest(node_2, poly_sum)
    else:
        raise RuntimeError("Invalid parameters")

    return poly_sum
