import pytest

from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(3, 4) == -1

    def test_division_success(self):
        assert self.calc.division(8, 2) == 4

    def test_multiply_success(self):
        assert self.calc.multiply(5, 6) == 30

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)
