In Python, **packing** and **unpacking** refer to the process of handling variable-length collections of items (such as tuples, lists, or dictionaries) in a flexible way. This is most commonly seen with function arguments and variable assignments.

# ### 1. Packing
# Packing is the process of grouping multiple values into a single collection, like a tuple or list.
#
# #### Example:
# ```python
# # Packing multiple variables into a tuple
# a = 1
# b = 2
# c = 3
# packed_tuple = a, b, c
# print(packed_tuple)  # (1, 2, 3)
# ```
#
# In function definitions, you can also "pack" multiple arguments into a tuple or list:
#
# ```python
# def my_function(*args):
#     print(args)
#
# my_function(1, 2, 3, 4)
# # Output: (1, 2, 3, 4)
# ```
#
# The `*args` syntax packs all positional arguments into a tuple.
#
# ### 2. Unpacking
# Unpacking is the reverse of packing. It involves extracting the values from a collection and assigning them to individual variables.
#
# #### Example:
# ```python
# # Unpacking a tuple
# packed_tuple = (1, 2, 3)
# a, b, c = packed_tuple
# print(a, b, c)  # 1 2 3
# ```
#
# In function calls, you can use **unpacking** to pass arguments from a collection (e.g., a tuple or list) to a function:
#
# ```python
# def add(x, y, z):
#     return x + y + z
#
# params = (1, 2, 3)
# print(add(*params))  # 6
# ```
#
# ### Advanced Unpacking
# Python allows for more advanced unpacking using `*` and `**`:
#
# #### 1. Unpacking with `*` for variable-length arguments:
# ```python
# # Unpacking with * in function arguments
# def my_function(a, b, *args):
#     print(a, b)
#     print(args)
#
# my_function(1, 2, 3, 4, 5)
# # Output:
# # 1 2
# # (3, 4, 5)
# ```
#
# Here, `a` and `b` are assigned from the first two arguments, and `*args` collects the rest into a tuple.
#
# #### 2. Unpacking with `**` for dictionaries (keyword arguments):
# ```python
# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old!")
#
# info = {"name": "Alice", "age": 30}
# greet(**info)
# # Output: Hello Alice, you are 30 years old!
# ```
#
# ### 3. Unpacking in List Assignments:
# You can also use unpacking to assign parts of a list to variables:
#
# ```python
# # Unpacking with * to collect excess elements in a list
# a, b, *rest = [1, 2, 3, 4, 5]
# print(a, b)      # 1 2
# print(rest)      # [3, 4, 5]
# ```
#
# This can be useful when you want to capture the "extra" elements in a list.
#
# ### 4. Unpacking in Loops
# You can also unpack elements when iterating over a list of tuples (or lists):
#
# ```python
# pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
# for number, letter in pairs:
#     print(number, letter)
# ```
#
# This will output:
# ```
# 1 a
# 2 b
# 3 c
# ```
#
# ### Summary
# - **Packing**: Grouping multiple values into a collection, like using `*args` in function definitions.
# - **Unpacking**: Extracting values from a collection and assigning them to variables using `*args` or unpacking directly (e.g., `a, b, c = tuple`).
# - You can also use `*` to collect excess values in lists or function arguments and `**` for unpacking dictionaries.

