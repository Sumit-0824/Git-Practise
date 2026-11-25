# #count total no of uppercae and lower case
# sentence="Hello World Welcome To Python"
from re import *
# print(len(findall(r'[A-Z]','Hello World Welcome To Python')))  #5
# print(len(findall(r'[a-z]','Hello World Welcome To Python')))  #20
#
# #Using function
# # import re
# #
# #
# # def count_case_characters(text):
# #     # Count uppercase letters
# #     uppercase_count = len(re.findall(r'[A-Z]', text))
# #     # Count lowercase letters
# #     lowercase_count = len(re.findall(r'[a-z]', text))
# #
# #     return uppercase_count, lowercase_count
# #
# #
# # # Example usage:
# # text = "Hello World! This is a Test."
# # uppercase, lowercase = count_case_characters(text)
# #
# # print(f"Uppercase count: {uppercase}")
# # print(f"Lowercase count: {lowercase}")
#
# #Count no of white space
# sentence = "Hello world welcome to Python Hi How are you. Hi how are you"
#
# print(len(findall(r' ',sentence))) #12
#
#
# #Sum of all the number in below string
# #using for loop
# word = "Pytho12nReg567exp2" # 1+2+5+6+7+2
# num=0
# for ele in word:
#     if ele.isdigit():
#         num= num+int(ele)
# print(num)  #23
# #Using regular expression
# d= findall(r'[0-9]',word)
# print(sum([int(i)for i in d]))    #23
#
#
# # import re
# # def sum_of_numbers(text):
# #     # Find all sequences of digits in the text
# #     numbers = re.findall(r'\d+', text)
# #
# #     # Convert them to integers and sum them
# #     total_sum = sum(map(int, numbers))
# #
# #     return total_sum
# #
# #
# # # Example usage:
# # word = "Pytho12nReg567exp2"
# # total = sum_of_numbers(word)
# #
# # print(f"Sum of all numbers: {total}")
#
# #Sum of all the number in below string
# word = "Pytho12nReg567exp2"  # 12+567+2
# d= findall(r'[0-9]+',word)
#print(sum([int(i)for i in d]))   #581

sentence = 'hello@world! welcome!!! Python$ hi26 how are you & where are you'
print(findall(r'[^A-Za-z0-9]',sentence))

'hello world hi hello universe how are you happy birthday'
print(findall(r'\bh[a-zA-Z]+','hello world hi hello universe how are you happy birthday'))  #['hello', 'hi', 'hello', 'how', 'happy']
print(findall(r'[a-zA-Z]+y\b','hello world hi hello universe how are you happy birthday'))  #['happy', 'birthday']