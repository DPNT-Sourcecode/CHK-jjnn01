from lib.solutions.CHK import checkout_solution

class TestCHK():
    def test_singleA(self):
        assert checkout_solution.hello('John') == 'Hello, John!'
