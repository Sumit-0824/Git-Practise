# Regular expression : it is a sequence of charters that form a search pattern.

from re import findall
print(findall(r'the',"the theory of relativity"))    #['the', 'the']
print(findall(r'cat',"The dragging belly indicates your cat is too fat")) #['cat', 'cat']
print(findall(r'aeiou','hello how are you doing anna'))  #[]

# charater set : []
print(findall(r'[aeiou]','hello how are you doing anna')) #['e', 'o', 'o', 'a', 'e', 'o', 'u', 'o', 'i', 'a', 'a']
print(findall(r'[sS]mith','smith and blackSmith'))   #['smith', 'Smith']
print(findall(r'gr[ea]y','grey  gray'))              #['grey', 'gray']
print(findall(r'[0123456789]','The cost of the book is Rs.100')) #['1', '0', '0']
#
# range:-
print(findall(r'[0-9]','The cost of the book is Rs.100'))        #['1', '0', '0']
print(findall(r'[A-Z]','The cost of the book is Rs.100'))        #['T', 'R']
print(findall(r'[a-z]','The cost of the book is Rs.100'))        #['h', 'e', 'c', 'o', 's', 't', 'o', 'f', 't', 'h', 'e', 'b', 'o', 'o', 'k', 'i', 's', 's']

#count total number of Uppercase and lowercase letter
sentence = "Hello World Welcome To Python"
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

# count the number of white space
sentence = "Hello world welcome to Python Hi  How are you. Hi how are you"
print(len(findall(r' ',sentence)))                     #13

# ------------------------------------------------------------------------------
# meta charater : '+' --> matches 1 or more occurances of previous expression
print(findall(r'[0-9]+','The cost of the book is Rs.100'))    #['100']
print(findall(r'[a-z]+','The cost of the book is Rs.100'))    #['he', 'cost', 'of', 'the', 'book', 'is', 's']
print(findall(r'an+a','annnnna'))                             #['annnnna']

# --------------------------------------------------------------------------------
# sum all the number in the below string.
word = "Pytho12nReg567exp2"
# 1+2+5+6+7+2
d = findall(r'[0-9]',word)
print(sum([int(i)for i in d]))         #23

word = "Pytho12nReg567exp2"
# 12+567+2
d = findall(r'[0-9]+',word)
print(sum([int(i)for i in d]))          #581
# ----------------------------------------------------------------------------
# meta charater '?':matches 0 or 1 occurances of previous expression
print(findall(r'colou?r','color colour'))             #['color', 'colour']
print(findall(r'an?a','anna'))                         #[]
print(findall(r'https?','http://www.google.com'))      #['http']

print(findall(r'[0-9]+','The $cost of the book is Rs.100')) #['100']

# negation:^
print(findall(r'[^A-Za-z]+','The $cost of the book is Rs.100')) #[' $', ' ', ' ', ' ', ' ', ' ', '.100']
word = '@hello12world34welcome!123'
print(findall(r'[^A-Za-z]',word))  #['@', '1', '2', '3', '4', '!', '1', '2', '3']

sentence = 'hello@world! welcome!!! Python$ hi26 how are you & where are you?'
print(findall(r'[^A-Za-z0-9]',sentence))  #['@', '!', ' ', '!', '!', '!', ' ', '$', ' ', ' ', ' ', ' ', ' ', '&', ' ', ' ', ' ', '?']

# ---------------------------------------------------------------------------
# word boundary : (\b): transition b/w non-word char to word char or word char to non-word char

print(findall(r'\bday\b',"what a beautiful day today is"))                    #['day']
print(findall(r'\bh[a-zA-Z]+','hello world hi hello universe how are you happy birthday'))  #Starting with before\bchar[]
print(findall(r'[A-Za-z]+y\b','hello world hi hello universe how are you happy birthday'))  #Starting with before[]char#Starting with before\b[]

sentence = "hello hi american english and indian ocean united states"
print(findall(r'\b[aeiou][a-zA-Z]+',sentence))  #['american', 'english', 'and', 'indian', 'ocean', 'united']
#starting with vowel


sentence = "hello hi how are you what is your name he is older than me how old are you"
print(findall(r'\b[A-Za-z]{3}\b',sentence))   #['how', 'are', 'you', 'how', 'old', 'are', 'you']

print(findall(r'\b[A-Z]+\b',"This is PYTHON programming LANGUAGE and REGEX"))
#['PYTHON', 'LANGUAGE', 'REGEX']
print(findall(r'\b[a-z]+\b',"This is PYTHON programming LANGUAGE and REGEX"))
#['is', 'programming', 'and']
# --------------------------------------------------------------------------------------
print(findall(r'[0-9]+',"654 this string is starting with 12 and ending with numbers 289423784612 890"))
#['654', '12', '289423784612', '890']
print(findall(r'\d+',"654 this string is starting with 12 and ending with numbers 289423784612 890"))
#['654', '12', '289423784612', '890']

print(findall(r'\b\d{3}\b',"654 this string is starting with 12 and ending with numbers 289423784612 890"))
#['654', '890']
sentence = "my pan number is ABCDE1234X and the other number is XYZTR3104J id is 123XYZTR3104J89"
print(findall(r'\b[A-Z]{5}\d{4}[A-Z]\b',sentence))     #['ABCDE1234X', 'XYZTR3104J']

sentence = "hello hi how are you what is your name he is older than me how old are you"
print(findall(r'\b[a-z]{3}\b', sentence))   #['how', 'are', 'you', 'how', 'old', 'are', 'you']

# -----------------------------------------------------------------------------------
# meta  char '*':0 or more occurrences of previous expression
sentence = "he helps the community and he is the hero of the day"
print(findall(r'\bhe[A-Za-z]*',sentence))
#['he', 'helps', 'he', 'hero']


# --------------------------------------------------------------------------------------


