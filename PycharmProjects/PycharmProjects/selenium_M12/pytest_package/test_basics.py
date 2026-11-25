"""
Steps to create and run the pytest and generate report
1.create python package(__init__- it should be created by default
2.create file with test_(filename)
3. create test case with def test_(testcase)
4.To run we should use command line-go to terminal from right click-->open in--->Terminal
5.Command-pytest test_basics.py            it will not give the detailed report
6.For detailed report
-v    verbosity  :detailed information about the testcase
 s==   scripting :to print all the print statement in the console

 commands-pytest test_filename.py -vs

 To generate html report
1.Install pytest html in cmd                 pip install pytest-html
2. check installation successful             pip list
3. Install in terminal in editor             pip install pytest-html

To run
right click-->open in-->Terminal
pytest test_filename.py -vs --html="report_name.html"

To group all testcase under 1
1Create class with TestClassname:
2.Write all testcase under the class with (self)

Difference between pytest and python
1.Class name startwith Test prefix in pytest
2.In pytest it will execute all the testcase even some error detected
3.function name starts with test_ prefix
4.filename should always starts with test_filename in pytest

"""


class TestDemo:
    def test_spam(self):
        print("in spam")

    def test_assert(self):
        assert 2 == 3, "2 is not equal to 3"

    def test_greet(self):
        print("in greet")


