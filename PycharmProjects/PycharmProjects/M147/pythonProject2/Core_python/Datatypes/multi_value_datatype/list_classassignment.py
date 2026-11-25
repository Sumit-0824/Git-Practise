# Class assignment
#list Slicing
# names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
# # 1. Reverse the above list.
# print(names[::-1])
# #['microsoft', 'instagram', 'facebook', 'amazon', 'yahoo', 'google', 'apple']
# # 2. What is the output of names[2][3]
# print(names[2][3])
# # o
# # 3. What is the output of
# #a. names[-2: 3]
# print(names[-2: 3])
# #[]
# # 	b. names[-6:5]
# print(names[-6: 5])
# # ['google', 'yahoo', 'amazon', 'facebook']
# # 	c. names[-1:2:-1]
# print(names[-1:2:-1])
#['microsoft', 'instagram', 'facebook', 'amazon']
# 	d. names[13]
#print(names[13])
#IndexError-list out of range
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
# 	e. names[:2] = ['unknown', 'Unknown']
names[:2] = ['unknown', 'Unknown']
print(names)
#['unknown', 'Unknown', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

print("******************Methods***************")


# Methods in list
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
# 	1. What is the output of:
# 			a. names.append(['netflix', 'walmart', 'kroger’])
names.append(['netflix', 'walmart', 'kroger'])
print(names)
#Ans--->['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', ['netflix', 'walmart', 'kroger']]
# 			b. names.extend(['netflix', 'walmart', 'kroger'])
names.extend(['netflix', 'walmart', 'kroger'])
print(names)
#Ans---->['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', ['netflix', 'walmart', 'kroger'], 'netflix', 'walmart', 'kroger']
# 	2. What is the difference between pop, remove.
#Ans--->pop-erase the remove the element from the collection and return where as by using remove method we can remove the particular element from collection by giving particular index
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
# 	3. Sort the above list in descending order.
names.sort(reverse=True)
print(names)

#Ans--->['yahoo', 'microsoft', 'instagram', 'google', 'facebook', 'apple', 'amazon']
# 	4. Sort the above list in ascending order according to their length.

names.sort(key=len)      #reverse not required
print(names)
#Ans--->['yahoo', 'apple', 'google', 'amazon', 'facebook', 'microsoft', 'instagram']
# 	5. Sort the above list in descending order according to their length.
names.sort(key=len,reverse=True)
print(names)
#---->['microsoft', 'instagram', 'facebook', 'google', 'amazon', 'yahoo', 'apple']

string = "Hi welcome to python"
# 		a. Create a list with each character of the string as its element.
# 		o/p ['h','i',' ' ,'w'.....]
#print(','.join(string))            #Ans---->H,i, ,w,e,l,c,o,m,e, ,t,o, ,p,y,t,h,o,n
print(list(string))                #['H', 'i', ' ', 'w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n']

#         b. Create a list with each word of the string as its element.
print(string.split())
#Ans--->['Hi', 'welcome', 'to', 'python']
#         o/p ['hi','welcome','to','python']
