# set comprehension:it is phenomenon of creating a new set collection by
# # reducing the number of instruction

# syntax:
# var_name = {exp <for loop>}
# var_name = {exp <for loop> <if condition>}
# var_name = {Texp <if condition><else> Fexp <for loop>}

#1.WAPT to return a set of cube values

l = [3,4,5,6,7,3,4,2]
cube = {num**3 for num in l}
print(cube)

#Output-{64, 8, 343, 216, 27, 125}
#2.WAPT check given words from string are starting with consonents or not ,if it
# is starting with consonents ,add tuples having word and its length to a set
s = 'hai hello good morning this is python class'
t={(word,len(word))for word in s.split() if word[0] not in 'aeiou'}
print(t)
#{('good', 4), ('hello', 5), ('this', 4), ('class', 5), ('hai', 3), ('python', 6), ('morning', 7)}
#3.#WAPT check names are ending with 'a' or not if it is  ending with a add reversed name
# #else add as it is to a set
names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft','chitra', 'harshitha']
new_set=[name[::-1] if name[-1]== 'a' else name for name in names]
print(set(new_set))
#output--{'yahoo', 'flipkart', 'gmail', 'microsoft', 'apple', 'instagram', 'google', 'artihc', 'ahtihsrah'}
#4.#WAPT create a set of numbers which are dividing with 6 or 9 till 50 that should
# be unique
num={num for num in range(1,50) if num%6==0 or num%9==0}
print(num)

##Output-{36, 6, 9, 42, 12, 45, 48, 18, 24, 27, 30}
#Solve the question of list using set comprehension

#dict_Comprehension

words="this is a bunch of words"
d={word:len(word)for word in words.split()}
print(d)
##output--{'this': 4, 'is': 2, 'a': 1, 'bunch': 5, 'of': 2, 'words': 5}
d = {'a':1,'b':2,'c':3}
d1={v:k for k,v in d.items()}
print(d1)
#{1: 'a', 2: 'b', 3: 'c'}
my_string = 'guido van rossum'
#USING STRING
s=''
for char in my_string:


    if char not in s:
        s=s+char+str(my_string.count(char))
print(s)
#Using dictionary for loop
s1={}

for char in my_string:
    s1[char]=my_string.count(char)
print(s1)
##Output-{'g': 1, 'u': 2, 'i': 1, 'd': 1, 'o': 2, ' ': 2, 'v': 1, 'a': 1, 'n': 1, 'r': 1, 's': 2, 'm': 1}
#USING Dictionary comprehension
print({char:my_string.count(char) for char in my_string})
##Output-{'g': 1, 'u': 2, 'i': 1, 'd': 1, 'o': 2, ' ': 2, 'v': 1, 'a': 1, 'n': 1, 'r': 1, 's': 2, 'm': 1}

sentence = 'hello world welcome to python hello hi world welcome to python'
#Lenth of word
new_setence={word: len(word) for word in sentence.split() }
print(new_setence)

#output-{'hello': 5, 'world': 5, 'welcome': 7, 'to': 2, 'python': 6, 'hi': 2}
#Count of no. of times
new_setence={word: sentence.count(word) for word in sentence.split() }
print(new_setence)
#Output-{'hello': 2, 'world': 2, 'welcome': 2, 'to': 2, 'python': 2, 'hi': 1}
##Dictionary of char and ASCII Pair
S2='ABCabc'
new_s={char: ord(char) for char in S2}
print(new_s)
##Output-{'A': 65, 'B': 66, 'C': 67, 'a': 97, 'b': 98, 'c': 99}

