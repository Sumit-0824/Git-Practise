#Any pytest file should start with test_ or end with _test.py
#any test function should start with test_ to be recognized by pytest
#any method should be wrapped in test function to be recognized by pytest
#Different ways to run the test:
#1.To run the test, use the command: pytest -v test_demo.py
#2.To run the test and generate an HTML report, use the command: pytest -v --html=report.html test_demo.py
#3.to run the test using pytest Ui navigate to the test_demo.py file and right click and select run pytest in terminal
#4.edit configuration>click on + the select pytest and give the name of the test file and click on ok and then run the test
#Run specific test function from the test file using the command: py.test -k test_firstprogram -v -s
#run specific testcase py.test test_demo.py-v -s
#-k is used to run specific test case from the test file,
# -s is used to print the output in the terminal, -v is used to print the test case name in the terminal,
# -v is used to print the test case name in the terminal
#pytest.mark.skip is used to skip the test case,
# pytest.mark.xfail is used to mark the test case as expected to fail,
# pytest.mark.parametrize is used to run the test case with multiple data sets,
# pytest.mark.usefixtures is used to use the fixture in the test case,
# pytest.mark.run is used to run the test case in a specific order,
# pytest.mark.dependency is used to run the test case based on the dependency of other test cases,
# pytest.mark.timeout is used to set the timeout for the test case,
# pytest.mark.flaky is used to rerun the test case if it fails,
# pytest.mark.asyncio is used to run the test case asynchronously,
# pytest.mark.skipif is used to skip the test case based on a condition,
# pytest.mark.filterwarnings is used to filter warnings in the test case,
# pytest.mark.hookwrapper is used to wrap a hook function in the test case,
# pytest.mark.tryfirst is used to run the hook function before other hook functions,
# pytest.mark.trylast is used to run the hook function after other hook functions,
# pytest.mark.usefixtures is used to use the fixture in the test case.

def test_firstprogram():
    print("Hello World")

def test_greet():
    print("good morning")

