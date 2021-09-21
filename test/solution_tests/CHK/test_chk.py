from lib.solutions.CHK import checkout_solution

class TestCHK():
    def test_singleA(self):
        assert checkout_solution.checkout('A') == 50


    def test_singleB(self):
        assert checkout_solution.checkout('B') == 30


    def test_singleC(self):
        assert checkout_solution.checkout('C') == 20


    def test_singleD(self):
        assert checkout_solution.checkout('D') == 15

    def test_twoA(self):
        assert checkout_solution.checkout('AA') == 100

    def test_threeA(self):
        assert checkout_solution.checkout('AAA') == 130

    def test_fourA(self):
        assert checkout_solution.checkout('AAAA') == 180

    def test_fiveA(self):
        assert checkout_solution.checkout('AAAAA') == 200

    def test_Oct8(self):
        assert checkout_solution.checkout('AAAAAAAA') == 330
    
    def test_twoB(self):
        assert checkout_solution.checkout('BB') == 45

    def test_multiple_discounts_when_nested(self):
        assert checkout_solution.checkout('ABABA') == 175

    def test_lowercase(self):
        assert checkout_solution.checkout('a') == -1

    def test_bad_input_negative_one(self):
        assert checkout_solution.checkout('e') == -1

    def singleF(self):
        assert checkout_solution.checkout('F') == 10

    def tripleF(self):
        assert checkout_solution.checkout('FFF') == 20

