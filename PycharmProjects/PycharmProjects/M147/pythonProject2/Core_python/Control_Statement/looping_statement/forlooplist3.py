## 1.Remove the duplicates from the list without using inbuit functions
#names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']

# l=[]
# for ele in names:
#     if ele not in l:
#         l.append(ele)
# print(l)
##['apple', 'google', 'yahoo', 'facebook', 'gmail']

#2.WAP to iterate through the list and build the new list only if the item has even character
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
#
# l = []
#
# for name in names:
#     if len(name)%2==0:
#         l.append(name)
# print(l)
#['google', 'flipkart', 'facebook', 'amazon']


# # 3."Write a program to reverse the list as below
# words = ["hi", "hello", "python"]
# o/p ['nohtyp', 'olleh', 'ih']
# l=[]
# i=0
# words=words[::-1]
# for word in words:
#     l.append(words[i][::-1])
#     i+=1
# print(l)
# #['nohtyp', 'olleh', 'ih']
#4.Write a program to get the following output
##o/p-->'py','com','in','txt','csv'
# l = ['python.py', 'google.com', 'yahoo.in', 'file.txt' , 'file.csv']
#
# l1=[]
# for word in l:
#     s=word.split('.')
#     l1.append(s[1])
# print(l1)
#['py', 'com', 'in', 'txt', 'csv']



#5.WAP to get the output
#o/p-->a4b6c2d1
# string = 'aaaabbbbbbccd'
# s=''
# for char in string:
#     if char not in s:
#         s=s+char+str(string.count(char))
# print(s)

#Output-->a4b6c2d1
# #6.WAP to get the output
# string = 'aaaabbbbbbccd'
# # output: {'a':4 , 'b':6 , 'c':2 , 'd':1}
# d = {}
# # var[key] = value
# for char in string:
#     d[char] = string.count(char)
# print(d)
##Output-->{'a': 4, 'b': 6, 'c': 2, 'd': 1}

# 7.wap to get the following output
# s = 'python java web selenium SQL manual C++ jscript'
# #output: {'python':6 , 'java':4 , 'web':3, 'selenium': 8 , 'SQL':3 , 'manual':6 , 'C++':3, 'jscript':7}
# d={}
# words = s.split()
# print(words)
# ##-->['python', 'java', 'web', 'selenium', 'SQL', 'manual', 'C++', 'jscript']
#
# for word in words:
#     d[word]=len(word)   #count is used for sounting specific character and len is used for countint the no of char in word or string
# print(d)
#output--{'python': 6, 'java': 4, 'web': 3, 'selenium': 8, 'SQL': 3, 'manual': 6, 'C++': 3, 'jscript': 7}

#8.wap to get the following output
s = 'hello good evening'
##output: {'hello':'ho' , 'good':'gd' , 'evening' : 'eg'}
# d={}
# words=s.split()
#
# for word in words:
#     d[word]=word[0]+word[-1]
# print(d)
#{'hello': 'ho', 'good': 'gd', 'evening': 'eg'}
#########ASSIGNMENT################
#9. wap to extract a string starting with vowel character
# l = ['Apple' , 'Google' , 'amazon', 'instagram', 'gmail', 'Extract']
# l1=[]
# for word in l:
#     if word[0] in 'aeiouAEIOU':
#          l1.append(word)
# print(l1)
#output--->['Apple', 'amazon', 'instagram', 'Extract']

#10. wap to get the following output
l = ['python.py', 'google.com', 'yahoo.in', 'file.txt' , 'file1.csv']
#out: {'python':'py', 'google':'com', 'yahoo':'in', 'file':'txt', 'file1':'csv'}

# d={}
# for word in l:
#     k,v=word.split('.')
#     d[k]=v
# print(d)

##output--->{'python': 'py', 'google': 'com', 'yahoo': 'in', 'file': 'txt', 'file1': 'csv'}


