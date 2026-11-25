#Slicing-A process of extracting multiple character at a time
#Syntax:Var_name[Start index:end index(+/-1):step value]
#Start index- 1st index(+,-)
#End index- +1 in case of forward slicing
#End index- -1 in case of negative slicing
#0          len of coll       1

s= "Good Morning"


print(s[5::1])   #Morning
print(s[5:12:1])  #Morning
print(s[-7::1])   #Morning
print(s[-7:-1:1])  #Mornin
print(s[-4:1:-1])  #nroM do

print("*********************************")

print(s[::])    #Good Morning
print(s[::1])   #Good Morning
print(s[::2])   #Go onn
print(s[::3])   #Gdoi

print(s[::-1])  #gninroM dooG
print(s[::-2])  #girMdo
print(s[::-3])  #gnMo