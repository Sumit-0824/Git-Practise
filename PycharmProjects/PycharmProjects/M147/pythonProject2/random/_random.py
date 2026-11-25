import random
# print(dir(random))
# print(random.random())  #0-1                      #0.3187477360176446  -in range of 0 to 1
# print(random.uniform(1,100))                #37.54846925908542
# print(random.randint(1,20))                  #3  only in int
#print(random.randrange(0,45,2))    #30 only in int with multiple of 2 based on step
#
names = ['google','yahoo','microsoft','facebook','gmail']
print(random.choice(names))

#output---microsoft

values = [2,4,1,5,7,9,6,4]
random.shuffle(values)
print(values)
#[1, 7, 4, 2, 4, 5, 9, 6]
# #Generating the 4 digit otp
# def generate_otp():
#     otp=[]
#     for i in range(4):
#         otp.append(str(random.randint(0,9)))
#     return "".join (otp)
# print(generate_otp())
# #2nd Method
#
# print(random.randint(1000,9999))
#
# #Generating the 6 digit otp
# #1st Method
# def generate_otp():
#     otp=[]
#     for i in range(6):
#         otp.append(str(random.randint(0,9)))
#     return "".join (otp)
# print(generate_otp())
# #2nd Method
#
# print(random.randint(100000,999999))