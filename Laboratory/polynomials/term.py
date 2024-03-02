"""
this class represents the terms of a polynomial
"""


class Term:
    def __init__(self, coefficient: float, grade: int):
        self._grade = grade
        self._coefficient = coefficient
