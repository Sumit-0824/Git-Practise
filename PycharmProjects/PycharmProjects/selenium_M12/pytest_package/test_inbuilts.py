"""
1.skip- when we want to skip unconditionary
2.Skipif-particular conditions are required to skip the test case


@pytest.mark.skip(reason=" ")
@pytest.mark.skipif(condition,reason=" ")
command-pytest filename -vs
for report- pytest test_inbuilts.py -vs --html="inbuit.html"

"""


import pytest

a=10
b=5    #b= 0 for skipif

def test_add():
    assert a+b !=0, "Sum of a and b is 0"

@pytest.mark.skip(reason="test_sub is stable")
def test_sub():
    assert a-b >0, "b is greater than a"
    print(a-b)

def test_mul():
    assert a*b >0, "product of a and b is less than 0"
@pytest.mark.skipif(b==0,reason="denominator is 0")
def test_div():
    assert a/b, "quotient is equal to 1"