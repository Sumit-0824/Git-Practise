"""
pytest marker used to group the two test cases/test functions
2 types
1.Custom markers- User defined markers
2.inbuits markers- Predefined functions available

1. custom markers-It adds extra functionality to the existing function without modifying the original function or existing function
@pytest.mark.group_a----.group_a- custom
@pytest.mark.group_b----.group_b-custom


Executing for particular  group
pytest test_custom.py -vs -m "group_a"
pytest test_custom.py -vs -m "group_b"
Using operator running
pytest test_custom.py -vs -m "group_b or group_a"
pytest test_custom.py -vs -m "group_b and group_a"
To generate report-pytest test_custom.py -vs -m "group_b or group_a" --html="test_custom.html"
"""






import pytest

a=10
b=5
@pytest.mark.group_a
def test_add():
    assert a+b !=0, "Sum of a and b is 0"

@pytest.mark.group_a
@pytest.mark.group_b
def test_sub():
    assert a-b >0, "b is greater than a"
    print(a-b)
@pytest.mark.group_b
def test_mul():
    assert a*b >0, "product of a and b is less than 0"

@pytest.mark.group_a
def test_div():
    assert a/b, "quotient is equal to 1"

def test_greet():
    print("hello")

