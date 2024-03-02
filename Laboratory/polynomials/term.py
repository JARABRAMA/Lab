"""
this class represents the terms of a polynomial
"""


class Term:
    def __init__(self, coefficient: float, grade: int):
        self._GRADE = grade  # these values are constants and are private
        self._COEFFICIENT = coefficient

    def get_grade(self) -> int:
        return self._GRADE

    def get_coefficient(self) -> float:
        return self._COEFFICIENT


