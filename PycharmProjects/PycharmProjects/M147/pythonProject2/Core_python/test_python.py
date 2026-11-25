# #1.
# #1. Write a program to sum all even numbers in the given string
# #sentence = 'hello 123 world 567 welcome to 9724 python'
# count=0
# for char in sentence:
#     if char.isdigit() and  int(char)%2==0:
#         count=count+int(char)
# print(count)
#
# ##Output-14
# #2.Convert the string "Hello welcome to Python" to a comma separated string.
# s = "Hello welcome to Python"
# s1=''
# for ele in s:
#     s1=s.replace(' ',',')
# print(s1)
# ##Output-Hello,welcome,to,Python
# #5. Write a program to extract all the unique words which starts with letter 'h' in the given string using comprehension
# #string = 'hello world hi hello universe how are you happy birthday'
# s={word for word in string.split() if word[0].startswith('h')}
# print(s)
# ##output-{'hi', 'how', 'happy', 'hello'}
# #6. Write a Program to print ascii values of the characters present in a string.(by using comp
# #sentence = "Hi How are you"
# print([ord(char) for char in sentence])
# #Output-[72, 105, 32, 72, 111, 119, 32, 97, 114, 101, 32, 121, 111, 117]
#
# #8.Write a program to get the below output
# #sentence = "hello world welcome to python programming hi there"
# #d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python", "programming"]}
#
# d={}
# for word in sentence.split():
#     first_char=word[0]
#     if first_char in d:
#         d[first_char].append(word)
#     else:
#         d[first_char] = [word]
# print(d)
##Output-{'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming']}
#10. Write a python program to get the below outputs
sentence ="Hi How are you"
#o/p should be "ouy era woH iH"

i=0
while i<len(sentence):
    sentence=sentence[::-1]
    i=+1
print(sentence,end=' ')


