# lambda expression / Anonymous function:
#A lambda expression (or lambda function) is a small, anonymous function in Python that can have any number of arguments but
# only one expression. Lambda functions are defined using the lambda keyword,
# followed by the arguments, a colon, and then the expression to be evaluated and returned.
#Iterable: An object that can be looped over, such as a list, tuple, string,set,dictionary.
# it is function that define without the name.
# syntax:
# var_name = lambda arg : exp
#lambda arguments: expression

'''Key points:
Anonymous: Lambda functions are often used when you need a small function for a short period and don't want to define a full function using def.
One-line function: Lambda functions can only contain a single expression. They are not meant for complex operations.
Return value: The expression in the lambda is automatically returned, so you don't need to explicitly use the return keyword.
'''
##CHATGPT#####
### Common Uses:
#Lambda functions are commonly used with functions like `map()`, `filter()`, and `sorted()` for concise code. For example:

#### Using lambda with `map()`:
numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16]


#### Using lambda with `filter()`:
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]


#### Using lambda with `sorted()`:

points = [(2, 3), (4, 1), (5, 0), (1, 7)]
sorted_points = sorted(points, key=lambda x: x[1])  # Sort by the second value in each tuple
print(sorted_points)  # Output: [(5, 0), (4, 1), (2, 3), (1, 7)]
####CHATGPT#####


### Why use a lambda?
# Lambda functions are useful when:
# - You need a quick function for a one-time operation.
# - You want to avoid the overhead of defining a full function using `def`.
# - You prefer a more concise, inline way of defining simple functions.

# WAPT return square of given number
# def square(num):
#     return num**2
#
# print(square(4))

sq = lambda num : num**2
print(sq(7))

# Texp <if condition> <else> Fexp
# WAPT check palindrome or not
pali = lambda s :'palindrome' if s == s[::-1] else 'not a palindrome'
print(pali('anna'))

# WAPT return square of len of given call is even else cube
#  python->6**2  hai->3**3
res = lambda s :len(s)**2 if len(s)%2==0 else len(s)**3
print(res('python')) #36
print(res('hai'))#27

# WAPT return a dictionary of numbers and square of number pair
# [4,5,6,7,8]
# {4:16,5:25,6:36,..}
res = lambda lst:{ele:ele**2 for ele in lst}
print(res([4,5,6,7,8]))

#WAPT return dict of index and element pair
d=['sumit','kumar','sinha','Male','Bangalore']
dic= lambda d: {(i,v) for i,v in enumerate(d)}
print(dic(d))

#WAPT check given number is perfect squre or not
num=26
res = lambda n : 'perfect number' if (n**0.5)**2 == num else 'not a prefect number'
print(res(25))

#WAPT to return a string by reversing if it is having even length else
#return as it is
s='Hello Sumith Kumars Sinhaa how'
st= lambda s:[ele[::-1] if len(ele)%2==0 else ele for ele in s.split()]
print(st(s))


#WAPT return number of digit present in integer
# Lambda function to count digits in an integer
count_digits = lambda n: len(str(abs(n)))

# Test with an example
number = 12345
print(count_digits(number))  # Output: 5


# -----------------------------------------------------------------------------------------------
# map():map is function which is used to perform same set of operation for all the values
# present in the collection or iterable
# map function will take the two arguments,function name and collection
# syntax: map(fname,collection)
# note : in map length i/p collection == length of the o/p collection
#The map() function in Python is used to apply a given function (such as a lambda function) to each item in an iterable
# (like a list, tuple, or string) and return a map object (which is an iterator).
# It allows you to process each item of the iterable in a clean and efficient way.

### Syntax:
#map(function, iterable)


#**function**: A function (like a lambda) that is applied to each element of the iterable.
# **iterable**: The iterable whose items will be processed by the function.

### Using `map()` with Lambda:
#When you use `map()` with a lambda function, it allows you to apply the lambda to each element of the iterable without needing to define a separate function.

### Example:

numbers = [1, 2, 3, 4, 5]

# Using map() with lambda to square each number
squared_numbers = map(lambda x: x**2, numbers)

# Converting the map object to a list to see the results
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

### Explanation:
# - The `lambda x: x**2` is a lambda function that squares each number.
# - The `map()` function applies this lambda to every element in the `numbers` list.
# - The result of `map()` is a map object, which is an iterator. We convert it to a list using `list()` to view the output.

### Another Example (Converting Strings to Uppercase):
words = ["hello", "world", "python"]

# Using map() with lambda to convert each word to uppercase
uppercase_words = map(lambda word: word.upper(), words)

# Convert to list and print
print(list(uppercase_words))  # Output: ['HELLO', 'WORLD', 'PYTHON']
### More Examples:
#### Applying a function to two lists (multiple iterables):
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
# Using map() with lambda to add corresponding elements of two lists
sum_numbers = map(lambda x, y: x + y, numbers1, numbers2)
print(list(sum_numbers))  # Output: [5, 7, 9]

### Key Points:
#`map()` returns an iterator, so you often need to convert it to a list (or other collections) to see the results.
# It is commonly used for applying a function to every item in an iterable without explicitly writing a loop.

# WAPT square and cube every number in a given list of integers
nums = [1,2,3,4,5]
# def sq_cb(num):
#     return num**2,num**3
print(list(map(lambda n : (n**2,n**3),nums)))

# WAPT find if a given list of string starting with 'aA'
names =['Alex','steve','Anna','henry','john']
print(list(map(lambda name :name if name[0] in 'aA' else None ,names)))

#WAPT return a list of elements raised to the power of thier indices
nums = [1,2,3,4]
def index_power(item):
    index,value = item
    return value**index

print(list(map(index_power,enumerate(nums))))


# x = (index,value)

print(list(map(lambda x:x[1]**x[0],enumerate(nums))))

# wapt calculate the sum of only positive number of a given list
nums = [1,-8,3,4,-7,-12]
# map(),sum()
positive_sum = sum(map(lambda x: x if x > 0 else 0, nums))
print(positive_sum)

# ----------------------------------------------------------------------------------------
# filter : is function which is used to perform same set of operation for all the values
# # present in the collection or iterable

# syntax : var_name = filter(fname,coll)

#The `filter()` function in Python is used to filter elements from an iterable (like a list, tuple, or string) based on a condition. It returns an iterator that produces only the elements from the iterable for which the function (like a lambda function) returns `True`. Elements for which the function returns `False` are excluded from the result.

### Syntax:
#filter(function, iterable)


# - **function**: A function (often a lambda) that tests each element in the iterable. It should return `True` or `False`.
# - **iterable**: The iterable whose elements will be tested by the function.

### Using `filter()` with a Lambda Function:
# When combined with a lambda function, `filter()` can be used to filter elements from the iterable based on simple, inline conditions.

### Example 1: Filtering Even Numbers from a List

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use filter() with lambda to get only even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert to list to view the result
print(list(even_numbers))  # Output: [2, 4, 6, 8]


### Explanation:
# - The lambda function `lambda x: x % 2 == 0` checks whether a number is even.
# - The `filter()` function applies this lambda to each element in the `numbers` list.
# - The result is an iterator, so we convert it to a list to see the filtered elements.

### Example 2: Filtering Strings with Length Greater Than 3
words = ["apple", "pie", "cat", "banana", "dog"]

# Use filter() with lambda to get words longer than 3 characters
long_words = filter(lambda word: len(word) > 3, words)

# Convert to list to view the result
print(list(long_words))  # Output: ['apple', 'banana']

### Example 3: Filtering Negative Numbers
numbers = [-1, -2, 3, 4, -5]

# Use filter() with lambda to get only negative numbers
negative_numbers = filter(lambda x: x < 0, numbers)

# Convert to list to view the result
print(list(negative_numbers))  # Output: [-1, -2, -5]

### Key Points:
# - `filter()` returns an iterator, not a list. You typically need to convert the result to a list (or other collection) to view it.
# - The function (or lambda) used with `filter()` should return a boolean value (`True` or `False`). If `True`, the element is included in the result; if `False`, it is excluded.
# - `filter()` is useful for filtering out unwanted items from a collection based on specific criteria.



# WAPT find if a given list of string starting with 'aA'
names =['Alex','steve','Anna','henry','john']
print(list(filter(lambda name : name[0] in 'aA' ,names)))

nums = [1,-8,3,4,-7,-12]
print(sum(list(filter(lambda x:x>0,nums))))

#built a list with only even length string using filter class
names = ['apple','google','yahoo','facebook','flipkart','gmail','instagram','microsoft']
print(list(filter(lambda name: len(name)%2==0,names )))

#return the string if the string is starting with vowel chrater
names = ['laura','steve','bill','james','bob','greg','scott','alex','ive']
print(list(filter(lambda name:name[0] in 'aeiou',names)))

# wapt print only even number in range 1-50 by using the filter
print(list(filter(lambda n :n%2==0,range(1,51))))


items = [[2,7],[7,3],[3,8],[8,7],[9,7],[4,9]]
print(sorted(items,key=lambda ele:ele[0]))


