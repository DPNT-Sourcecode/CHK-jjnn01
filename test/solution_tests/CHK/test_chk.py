from lib.solutions.CHK import hello_solution

class TestHLO():
    def test_hello(self):
        assert hello_solution.hello('John') == 'Hello, John!'
