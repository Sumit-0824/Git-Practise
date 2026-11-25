#1.WAPT handle error,if denominator is 0,make it as 1 if index is out of range return element in last postition
def division(numerator, denominator):
    try:
        if denominator == 0:
            denominator = 1
        result = numerator / denominator
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_element(my_list, index):
    try:
        if index < 0 or index >= len(my_list):
            return my_list[-1]
        return my_list[index]
    except Exception as e:
        print(f"Error: {e}")
        return None
print(division(10,0))   #10.0
print(get_element([1, 2, 3, 4, 5],index=10)) #5

#2.WAPT to take 2 number and return sum of 2 numbers,handle if any error occurs
def sum(num1, num2):
    try:
        result = num1 + num2
        return result
    except TypeError:
        print("Error: Both inputs must be numbers.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
num1 = 20
num2 = 5
result = sum(num1, num2)
if result is not None:
    print(f"The sum of {num1} and {num2} is {result}")
# #Output
# #The sum of 20 and 5 is 25

#3.WA decorator To validate name(name should have min 5 characters if it not raise a error)
def validate_name(func):
    def wrapper(name):
        if len(name) < 5:
            raise ValueError("Name must have at least 5 characters.")
        return func(name)
    return wrapper

@validate_name
def process_name(name):
    print(f"Name '{name}' is valid and processed.")

#print(process_name('Sum'))  #ValueError("Name must have at least 5 characters.")
#print(process_name('Sumith')) #Name 'Sumith' is valid and processed

#4.WA decorator to delay n sec to execute function(write parameterised decorator)
from time import sleep,time
def _delay(time_delay):
    def delay(func):
        def wrapper(*args,**kwargs):
            sleep(5)
            return func(*args,**kwargs)
        return wrapper
    return delay

@_delay(3)
def greet():
    return 'hello world'

print(greet())             #hello world

#5. WA decorator to check execution time of a program
from time import sleep,time

def measure_time(func):
    def inner(*args,**kwargs):
        startpoint = time()
        res = func(*args,**kwargs)
        endpoint = time()
        print(f'execution time of function {func.__name__}:{endpoint-startpoint}')
        return res
    return inner
@measure_time
def add(a,b,c):
    sleep(2)
    return a+b+c
print(add(10,20,2))
# #execution time of function add:2.0013809204101562
#32
#6. write a decorator to count how many time that function is executed
def counting(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        print(f"Function {func.__name__} has been called {wrapper.counter} times.")
        return func(*args, **kwargs)
    wrapper.counter = 0
    return wrapper

@counting
def greet(name):
    print(f"Hello, {name}!")

greet("Sumit")
greet("Suresh")
greet("Virat")
'''
Function greet has been called 1 times.
Hello, Sumit!
Function greet has been called 2 times.
Hello, Suresh!
Function greet has been called 3 times.
Hello, Virat!
'''
#8. write a program to generate random numbers in between given range.
import random
def random_numb(start, end, count=1):
    random_numbers = [random.randint(start, end) for _ in range(5)]
    return random_numbers

print(random_numb(1,20)) #[20, 18, 16, 20, 4]
#9.write a program to print largest even and largest odd number in a list.

def largest_even_odd(numbers):
    largest_even = None
    largest_odd = None

    for num in numbers:
        if num % 2 == 0:  # Even number
            if largest_even is None or num > largest_even:
                largest_even = num
        else:  # Odd number
            if largest_odd is None or num > largest_odd:
                largest_odd = num
    return largest_even, largest_odd

print(largest_even_odd([12, 3, 7, 8, 5, 10, 33, 4, 20]))  #(20, 33)

#11. Input
tuples = [("Alice", 25), ("Bob", 30), ("Carol", 20), ("David", 25)]

# Output
# [("Carol", 20), ("Alice", 25), ("David", 25), ("Bob", 30)]

tuples = [("Alice", 25), ("Bob", 30), ("Carol", 20), ("David", 25)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)

# Output
# [("Carol", 20), ("Alice", 25), ("David", 25), ("Bob", 30)]
#12. list1 = [1, 2, 3, 4]
#list2 = [10, 20, 30, 40]
#by using lambda.
# Output
# [10, 40, 90, 160]

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

result = map(lambda x, y: x * y, list1, list2)
print(list(result))         #[10, 40, 90, 160]

#13.
# Input list of strings
strings = ["hello", "", "world", "", "python"]
new_str = filter(lambda x: x != "", strings)
print(list(new_str))   #['hello', 'world', 'python']

#14. capitalize_words
# Input
words = ["apple", "banana", "cherry", "date"]
capitalize_words = lambda word: word.capitalize()
capitalized_words = map(capitalize_words, words)
print(list(capitalized_words))
# Output
# ["Apple", "Banana", "Cherry", "Date"]

#15.count_vowels  using a lambda function and map.
# Input
words = ["hello", "world", "python", "programming"]

count_vowels = lambda word: sum(1 for char in word if char in 'aeiouAEIOU')

vowel_counts = map(count_vowels, words)
print(list(vowel_counts))
# Output
# [2, 1, 1, 3]















