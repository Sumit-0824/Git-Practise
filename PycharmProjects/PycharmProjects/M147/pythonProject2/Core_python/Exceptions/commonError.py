# In Python, errors are typically classified into two categories:
#
# ### 1. **Syntax Errors**
#    - These occur when Python can't parse the code due to incorrect syntax.
#    - Example:
#      ```python
#      print("Hello, world"
#      ```
#      Here, the closing parenthesis is missing, so it raises a syntax error.
#
# ### 2. **Exceptions**
#    - Exceptions occur during the program execution and are typically errors related to logic or conditions that the program encounters while running.
#    - Common exception types include:
#
#    - **NameError**: Raised when a local or global name is not found.
#      ```python
#      print(x)  # If x is not defined
#      ```
#    - **TypeError**: Occurs when an operation or function is applied to an object of inappropriate type.
#      ```python
#      print('2' + 2)  # String and integer cannot be added
#      ```
#    - **ValueError**: Raised when a function receives an argument of correct type but inappropriate value.
#      ```python
#      int("abc")  # Cannot convert 'abc' to an integer
#      ```
#    - **IndexError**: Occurs when trying to access an element from a list using an invalid index.
#      ```python
#      my_list = [1, 2, 3]
#      print(my_list[5])  # Index out of range
#      ```
#    - **KeyError**: Raised when trying to access a dictionary with a key that does not exist.
#      ```python
#      my_dict = {"name": "Alice"}
#      print(my_dict["age"])  # Key 'age' doesn't exist
#      ```
#    - **AttributeError**: Raised when an invalid attribute reference is made.
#      ```python
#      "hello".length()  # String object has no 'length' method
#      ```
#    - **ZeroDivisionError**: Raised when dividing by zero.
#      ```python
#      print(1 / 0)  # Division by zero
#      ```
#    - **FileNotFoundError**: Occurs when trying to open a file that doesn’t exist.
#      ```python
#      open("nonexistent_file.txt")  # File not found
#      ```
#
# ### 3. **Logical Errors**
#    - These are mistakes in the program's logic that lead to incorrect behavior or results. The program will run without errors, but the output will be wrong.
#      - Example:
#        ```python
#        x = 5
#        y = 10
#        print(x - y)  # You wanted addition, but it subtracts.
#        ```
#
# ### 4. **ImportError** (and its subclasses like `ModuleNotFoundError`)
#    - Raised when importing a module that can't be found.
#
#      import nonexistent_module  # Module does not exist


# Errors in Python can be handled using **try-except** blocks, allowing you to catch and manage them effectively during runtime.


# age=int(input('Enter the age: '))
# print(age)

# def div(n1,n2):
#     try:
#         res=n1/n2
#         return res
#     except:
#
# print(div(10,5))


# def is_valid_email(email):
#     if "@" in email and "." in email.split('@')[-1]:
#         return True
#     else:
#         return False
#
# email = input("Enter an email: ")
#
# if is_valid_email(email):
#     print("The email ID is valid.")
# else:
#     print("The email ID is invalid.")

# email = input("Enter an email: ")
# if "@" in email and email.endswith('.com'):              #"." in email.split('@')[-1]
#     print('It is valid email id')
# else:
#     raise ValueError("It is invalid email id.")


age=int(input('Enter the age:'))
if age>18:
    print('login successfully')
else:
    raise Exception('You are not allowed')