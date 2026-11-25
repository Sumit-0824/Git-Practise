
# a = [3, 5, 4, 8, 11, 1, -1, 6]
# res = []
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] + a[j] == 10 or abs(a[i] - a[j]) == 10:
#             res.append((a[i], a[j]))
# print(res)
# #output-[(4, 6), (11, 1), (11, -1)]


# sentence = 'hello 123 world 456 welcome to python498675634'
# numb = []
# cnum = ''
# for char in sentence:
#     if char.isdigit():
#         cnum += char
#     else:
#         if cnum:
#             numb.append(cnum)
#             cnum = ''
# if cnum:
#     numb.append(cnum)
# even_numbers = list(filter(lambda x: int(x) % 2 == 0, numb))
# odd_numbers = list(filter(lambda x: int(x) % 2 != 0, numb))
#
# print("Even Numbers:", even_numbers)
# print("Odd Numbers:", odd_numbers)
# #output
# '''Even Numbers: ['456', '498675634']
# Odd Numbers: ['123'] '''

# numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]
# numbers.sort()
# max_sum = sum(numbers[-3:])
#
# min_sum = sum(numbers[:3])
#
# print("Maximum sum of 3 numbers:", max_sum)
# print("Minimum sum of 3 numbers:", min_sum)
# #output
# ''' Maximum sum of 3 numbers: 105
# Minimum sum of 3 numbers: 40 '''

# import re
# s = 'hello@world! welcome!!! Pythons hi how are you & where are you?'
# pattern = r'[a-zA-Z0-9 ]'
# non_special_chars = re.findall(pattern, s)
# count = len(non_special_chars)
#
# print(f"Number of non-special characters: {count}")
#
# #Output--Number of non-special characters: 56

# numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
# end_with_5 = [num for num in numbers if num.endswith('5')]
# print("Numbers ending with 5:", end_with_5)
# Numbers ending with 5: ['12345', '125', '905', '55', '5', '95655', '55555']

# def infinite_counter():
#     count = 1
#     while True:
#         yield count
#         count += 1
# gen = infinite_counter()
# for i in range(5):
#     print(next(gen))
#
# #Output-
# '''
# 1
# 2
# 3
# 4
# 5
# '''


# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y
#
# def multiply(x, y):
#     return x * y
#
# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     else:
#         return x / y
#
# def calculator():
#     print("Select operation:")
#     print("1. Add (+)")
#     print("2. Subtract (-)")
#     print("3. Multiply (*)")
#     print("4. Divide (/)")
#
#
#     choice = input("Enter choice (1/2/3/4): ")
#
#
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#
#
#     if choice == '1':
#         print(f"{num1} + {num2} = {add(num1, num2)}")
#     elif choice == '2':
#         print(f"{num1} - {num2} = {subtract(num1, num2)}")
#     elif choice == '3':
#         print(f"{num1} * {num2} = {multiply(num1, num2)}")
#     elif choice == '4':
#         print(f"{num1} / {num2} = {divide(num1, num2)}")
#     else:
#         print("Invalid input! Please select a valid operation.")
#
#
# if __name__ == "__main__":
#     calculator()

import copy
original_list = [1, 2, [3, 4]]

shallow_copied_list = copy.copy(original_list)
shallow_copied_list[2][0] = 99
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)

#Output
'''Original List: [1, 2, [99, 4]]
Shallow Copied List: [1, 2, [99, 4]]'''


# import copy
# original_list = [1, 2, [3, 4]]
# deep_copied_list = copy.deepcopy(original_list)
# deep_copied_list[2][0] = 99
# print("Original List:", original_list)
# print("Deep Copied List:", deep_copied_list)
# #Output
# '''Original List: [1, 2, [3, 4]]
# Deep Copied List: [1, 2, [99, 4]]'''

# class Employee:
#     total_employees = 0
#
#     # Constructor to initialize employee details
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#         # Increment the total employee count when a new employee is created
#         Employee.total_employees += 1
#
#     # Instance method to display employee details
#     def display_info(self):
#         print(f"Name: {self.name}, Position: {self.position}")
#
#     # Class method to change the total employee count
#     @classmethod
#     def update_total_employees(cls, new_count):
#         cls.total_employees = new_count
#         print(f"Updated total employees to {cls.total_employees}")
#
#     # Static method to calculate salary (doesn't depend on the class or instance)
#     @staticmethod
#     def calculate_salary(hours_worked, hourly_rate):
#         return hours_worked * hourly_rate
#
#
# # Creating two employee objects
# emp1 = Employee("Alice", "Manager")
# emp2 = Employee("Bob", "Developer")
#
# # Display information about individual employees
# emp1.display_info()
# emp2.display_info()
#
# # Accessing the class variable directly
# print(f"Total Employees: {Employee.total_employees}")
#
# # Using the class method to update the total employee count
# Employee.update_total_employees(50)
#
# # Using the static method to calculate salary
# salary1 = Employee.calculate_salary(40, 30)  # 40 hours at 30 per hour
# salary2 = Employee.calculate_salary(35, 25)  # 35 hours at 25 per hour
#
# print(f"Employee 1 Salary: ${salary1}")
# print(f"Employee 2 Salary: ${salary2}")
#
# # Accessing the updated total employees
# print(f"Updated Total Employees: {Employee.total_employees}")

# Parent class: Vehicle
# class Vehicle:
#     def start(self):
#         print("Vehicle is starting.")
#
#     def stop(self):
#         print("Vehicle is stopping.")
#
# # Child class: Car
# class Car(Vehicle):
#     # Overriding the start method in the parent class
#     def start(self):
#         print("Car is starting with ignition.")
#
#     # Overriding the stop method in the parent class
#     def stop(self):
#         print("Car is stopping with brakes.")
#
# # Creating objects of Vehicle and Car
# vehicle = Vehicle()
# car = Car()
#
# # Calling start and stop methods using the vehicle object (parent class)
# print("Calling start() and stop() on Vehicle object:")
# vehicle.start()  # Calls Vehicle's start method
# vehicle.stop()   # Calls Vehicle's stop method
#
# # Calling start and stop methods using the car object (child class)
# print("\nCalling start() and stop() on Car object:")
# car.start()      # Calls Car's overridden start method
# car.stop()       # Calls Car's overridden stop method
#
# # Parent class: Vehicle
# class Vehicle:
#     def start(self):
#         print("Vehicle is starting.")
#
#     def stop(self):
#         print("Vehicle is stopping.")
#
# # Child class: Car
# class Car(Vehicle):
#     # Overriding the start method in the parent class
#     def start(self):
#         print("Car is starting with ignition.")
#
#     # Overriding the stop method in the parent class
#     def stop(self):
#         print("Car is stopping with brakes.")
#
# # Creating objects of Vehicle and Car
# vehicle = Vehicle()
# car = Car()
#
# # Calling start and stop methods using the vehicle object (parent class)
# print("Calling start() and stop() on Vehicle object:")
# vehicle.start()  # Calls Vehicle's start method
# vehicle.stop()   # Calls Vehicle's stop method
#
# # Calling start and stop methods using the car object (child class)
# print("\nCalling start() and stop() on Car object:")
# car.start()      # Calls Car's overridden start method
# car.stop()       # Calls Car's overridden stop method




# import csv
# data = [
#     ['Name', 'Age', 'City'],  # Header row
#     ['Alice', 30, 'New York'],
#     ['Bob', 25, 'Los Angeles'],
#     ['Charlie', 35, 'Chicago'],
#     ['David', 40, 'San Francisco'],
#     ['Eve', 28, 'Austin']
# ]
#
# # Open a CSV file in write mode ('w')
# with open('people.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#
#     # Write the data to the CSV file
#     writer.writerows(data)
#
# print("5 lines written to people.csv successfully!")


# def count_words(st, word_list=None, word_count=None):
#     # Initialize word_list and word_count in the first call
#     if word_list is None:
#         word_list = st.split()  # Split the string into words
#         word_count = {}         # Dictionary to store word counts
#
#     # Base case: If word_list is empty, return the word_count dictionary
#     if not word_list:
#         return word_count
#
#     # Recursive case: Process the first word
#     word = word_list[0]
#     # If the word is already in the dictionary, increment its count
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
#     # Recur with the rest of the words
#     return count_words(st, word_list[1:], word_count)


# Input string
# st = 'python is very difficult'
# result = count_words(st)
# print(result

def count_words(st, word_list=None, word_count=None):
    if word_list is None:
        word_list = st.split()
        word_count = {}
    if not word_list:
        return word_count
    word = word_list[0]
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
    return count_words(st, word_list[1:], word_count)
st = 'python is very difficult'
result = count_words(st)
print(result)

''' Output
{'python': 1, 'is': 1, 'very': 1, 'difficult': 1}
'''



