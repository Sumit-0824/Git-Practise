import pytest


# def test_teardown():
#     print("Tearing down the test environment")
@pytest.mark.usefixtures("setup")
class TestClass:
    def test_greet(self):
        print("Good morning")

    def test_greet1(self):
        print("Good evening")

    def test_greet2(self):
        print("Good night")




