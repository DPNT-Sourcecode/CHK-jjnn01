from lib.solutions.SUM import sum_solution
import pytest

class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    inputs = [(0,0,0),(100,100,200),(0,100,100),(100,0,100),(33,47,80)]
    @pytest.mark.parametrize("first,second,solution", inputs)
    def test_sums(first, second, solution):
        assert sum_solution.compute(first, second) == solution


