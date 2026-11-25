"""
fixtures : function, to add setup and tear down functionality for the test cases
means to execute something before and after the test cases
syntax
@pytest.fixture(parameter) == create a new fixture
    1. autouse = automatically calls the fixture
    2. scope=

set up functionality : executes before the test case
tear down functionality : executes after the test case
"""


import pytest
# set up functionality :executes before the test
'''
Steps
1. create set up fixture  @pytest.fixture() for the set up testcase
2.Pass the set up fixture in the testcase as argument

'''

# @pytest.fixture()
# def greet():
#     print("hello")
#
# def test_add(greet):
#     print("in the test")
#
# def test_spam(greet):
#     print("in the spam")
#
'''
output
test_fixt.py::test_add hello
in the test
PASSED
test_fixt.py::test_spam hello
in the spam
PASSED
'''

####################################################################
#tear down functionality--It executes after the execution of testcase

# @pytest.fixture()
# def greet():
#     print("hello")         #set up functionality
#     yield
#     print("End")           #tear down functionlity
#
# def test_add(greet):
#     print("in the test")
#
# def test_spam(greet):
#     print("in the spam")

'''
Output
test_fixt.py::test_add hello
in the test
PASSEDEnd

test_fixt.py::test_spam hello
in the spam
PASSEDEnd

'''
#######################################################################
#Autouse- Automatically call the fixture
#It is used when we have multiple test case to execute
# @pytest.fixture(autouse=True)
# def greet():
#     print("hello")         #set up functionality
#     yield
#     print("End")           #tear down functionlity
#
# def test_add():
#     print("in the test")
#
# def test_spam():
#     print("in the spam")
'''
Output
test_fixt.py::test_add hello
in the test
PASSEDEnd

test_fixt.py::test_spam hello
in the spam
PASSEDEnd

'''
###############################################################################
#scope=class Defying the class
# @pytest.fixture(autouse=True,scope="class")
# def greet():
#     print("hello")         #set up functionality
#     yield
#     print("End")           #tear down functionlity
# class TestFixture:
#     def test_add(self):
#         print("in the test")
#
#     def test_spam(self):
#         print("in the spam")

'''
output
test_fixt.py::TestFixture::test_add hello
in the test
PASSED
test_fixt.py::TestFixture::test_spam in the spam
PASSEDEnd

'''
###############################################################################################
#scope=class Without Defying the class
# @pytest.fixture(autouse=True)
# def greet():
#     print("hello")         #set up functionality
#     yield
#     print("End")           #tear down functionlity
# class TestFixture:
#     def test_add(self):
#         print("in the test")
#
#     def test_spam(self):
#         print("in the spam")

'''
output
test_fixt.py::TestFixture::test_add hello
in the test
PASSEDEnd

test_fixt.py::TestFixture::test_spam hello
in the spam
PASSEDEnd
It will execute set up and tear down for all testcase

'''
#############################################################
#We we need to use only for particular class
# @pytest.fixture(scope="class")
# def greet():
#     print("hello")         #set up functionality
#     yield
#     print("End")           #tear down functionlity
#
# @pytest.mark.usefixtures("greet")
# class TestFixture:
#     def test_add(self):
#         print("in the test")
#
#     def test_spam(self):
#         print("in the spam")

'''
Output
test_fixt.py::TestFixture::test_add hello
in the test
PASSED
test_fixt.py::TestFixture::test_spam in the spam
PASSEDEnd
'''
###############################################################
@pytest.fixture
def greet():
    print("hello")         #set up functionality
    a=10
    yield a #a=10
    print("End")           #tear down functionlity

def test_add(greet):
    a=greet  #a=10
    print(a) #a=10
    print(greet)
    print("in the test add")

def test_spam(greet):
    print("in the spam")

'''
Output
test_fixt.py::test_add hello
10
10
in the test add
PASSEDEnd

test_fixt.py::test_spam hello
in the spam
PASSEDEnd


'''