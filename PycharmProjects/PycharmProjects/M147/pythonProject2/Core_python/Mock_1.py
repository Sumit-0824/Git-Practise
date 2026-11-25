PYTHON MOCK-1

1. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
    except the first char itself.
	s = 'restart'
	o/p : 'resta$t'

2. Write a Python script to add a key to a dictionary.
	Sample Dictionary : {0: 10, 1: 20}
	Expected Result : {0: 10, 1: 20, 2: 30}

3. Write a Python program to get the 4th element from the last element of a tuple.
	tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")


4. Write a Python program to convert a list to a tuple
	listx = [5, 10, 7, 4, 15, 3]

5. Does converting an object to a set maintain the object’s order?

6. Check if a specific value (7) exists in a set
	s ={1,2,3}

7. What is the output of the following
	aTuple = (10, 20, 30, 40, 50, 60, 70, 80)
	print(aTuple[2:5], aTuple[:4], aTuple[3:])
  a. (30, 40, 50) (10, 20, 30, 40) (40, 50, 60, 70, 80)
  b. (20, 30, 40, 50) (10, 20, 30, 40) (30, 40, 50, 60, 70, 80)
#Ans-a. (30, 40, 50) (10, 20, 30, 40) (40, 50, 60, 70, 80)
8. A Python tuple can also be created without using parentheses
  a. False
  b. True

9. What is the output of the following tuple operation
	aTuple = (100,)
	print(aTuple * 2)
  a. TypeError
  b. (100, 100)
  c. (200)

10. What is the type of the following variable
	aTuple = ("Orange")
	print(type(aTuple))
  a. list
  b. tuple
  c. array
  d. str

11. Choose the correct function to get the ASCII code of a character
  a. char('char')
  b. ord('char')
  c. ascii('char')

12. Select the correct output of the following String operations
	str = "my name is James bond"
	print (str.capitalize())
  a. My Name Is James Bond
  b. TypeError: unsupported operand type(s) for * or pow(): 'str' and 'int'
  c. My name is james bond

13. Guess the correct output of the following code?
	str1 = "PYnative"
	print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])
  a. PYn PYnat ive PYnativ vitanYP
  b. Yna PYnat tive PYnativ vitanYP
  c. Yna PYnat tive PYnativ PYnativ

14. What is the output of the following list operation
	sampleList = [10, 20, 30, 40, 50]
	print(sampleList[-2])
	print(sampleList[-4:-1])
  a. 40
    [20, 30, 40]
  b. IndexError: list index out of range

15. Select all the correct options to join two lists in Python
	listOne  =  ['a', 'b', 'c', 'd']
	listTwo =  ['e', 'f', 'g']
  a. newList = listOne + listTwo
  b. newList = extend(listOne, listTwo)
  c. newList = listOne.extend(listTwo)
  d. newList.extend(listOne, listTwo)

16. What is the output of the following dictionary operation
	dict1 = {"name": "Mike", "salary": 8000}
	temp = dict1.get("age")
	print(temp)
  a. KeyError: ‘age’
  b. None

17. Select the correct ways to get the value of marks key.
	student = {
  	"name": "Emma",
  	"class": 9,
  	"marks": 75
	}
  a. m = student.get(2)
  b. m = student.get('marks')
  c. m = student[2])
  d. m = student['marks'])

18. Take input of age of 3 people by user and determine oldest and youngest among them.

19. Take values of length and breadth of a rectangle from user and check if it is square or not.

20. Write a program to print absolute vlaue of a number entered by user.
 E.g.-
	INPUT: 1        OUTPUT: 1
	INPUT: -1        OUTPUT: 1


21. Write a program to check if a year is leap year or not.
NOTE: If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

22. A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one.
E.g.-
	INPUT : 1234        OUTPUT : 4321
	INPUT : 5982        OUTPUT : 2895
