# dict_comprehension:it is a phenomenon of creating a new dicit collection by
# reducing the number of instruction

# syntax:
# var_name = {key:value <for loop>}
# var_name = {key:value <for loop> <if condition>}
# var_name = {key:value <if condition> <else> value <for loop>}

# 1.Building a dict of word and length pair
words = "this is a bunch of words"
# #o/p:{'this':4,'is':2,'a':1,'bunch':5..}
d = {word:len(word) for word in words.split()}
print(d)

# #2.Flipping keys and values of the dictionary using dict comprehension
d = {'a':1,'b':2,'c':3}
# #o/p:{1:'a',2:'b',3:'c'}
print({v:k for k,v in d.items()})

# 3.Counting the number of each character in a String
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

# 4.Counting the number of each word in a String
sentence = 'hello world welcome to python hello hi world welcome to python'

#Lenth of word
new_setence={word: len(word) for word in sentence.split() }
print(new_setence)

#output-{'hello': 5, 'world': 5, 'welcome': 7, 'to': 2, 'python': 6, 'hi': 2}
#Count of no. of times
new_setence={word: sentence.count(word) for word in sentence.split() }
print(new_setence)
#Output-{'hello': 2, 'world': 2, 'welcome': 2, 'to': 2, 'python': 2, 'hi': 1}

#5. Dictionary of character and ascii value pairs
s ='ABCabc'
# #o/p:{'A':65,..}
S2='ABCabc'
new_s={char: ord(char) for char in S2}
print(new_s)
##Output-{'A': 65, 'B': 66, 'C': 67, 'a': 97, 'b': 98, 'c': 99}
#6.

cities = ['Tokyo',
         'Delhi',
         'Shanghai',
         'Sao Paulo',
         'Mumbai'
         ]
populations = ['38,001,000',
             '25,703,168',
             '23,740,778',
             '21,066,245',
             '21,042,538'
             ]


cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai' ]
populations = ['38,001,000', '25,703,168', '23,740,778', '21,066,245', '21,042,538' ]
print({v1:v2 for v1,v2 in zip(cities,populations)})
##Output--{'Tokyo': '38,001,000', 'Delhi': '25,703,168', 'Shanghai': '23,740,778', 'Sao Paulo': '21,066,245', 'Mumbai': '21,042,538'}
#Same as above print({city:pop for city,pop in zip(cities,populations)})


# 7.building a dict whose price value is more than 200
prices = {'ACME':45.23,'AAPL':612.78,'IBM':205.55,'HPQ':37.20,'FQ':10.75}
new_dict={k:v for k,v in prices.items()  if v >200 }
print(new_dict)
#{'AAPL': 612.78, 'IBM': 205.55}


