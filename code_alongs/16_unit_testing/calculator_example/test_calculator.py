from calculator import Calculator

calc = Calculator()

def test_addition():
    num1 = 5
    num2 = 3
    assert calc.add(num1,num2) == num1+num2

def test_add_negative():
    num1 = -5
    num2 = -3
    assert calc.add(num1,num2) == num1+num2