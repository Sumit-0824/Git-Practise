s="International"

print(s[0:])
print(s[1:])

print("*********************Positive slicing************************")
#nternatio
print(s[1:10])
#terna
print(s[2:7:1]) #0r print(s[2:7])
#tional
print(s[7::1])
##tional
print(s[-6:])
#tional
print(s[-3:2:-1])

#2
k= 'SUMIT KUMAR'
####################Slicing######################################
#KUMAR
print(k[-5::1])
print(k[6::1])
#RAMUK
print(k[-1:-6:-1])
#IT KUM
print(k[3:-2:1]) #end index= -3+1
print(k[3:9]) # or print(k[3:9:1]
#MUK TI
print(k[-3:2:-1])  #end index=3-1

print("####################Skipping######################################")
print(k[::1])  #SUMIT KUMAR
print(k[::2])  #SMTKMR
print(k[::3])  #SIKA
print(k[::4])  #STM

print(k[::-1])  #RAMUK TIMUS
print(k[::-2])  #RMKTMS
print(k[::-3])  #RUTU
print(k[::-4])  #RKM

#String formatting:Infusding the data dynamically into a string during the time of execution

#Prefixed with f
#{}-Placeholder
#Example 1
first_name='sumit'

print(f'Welcome{first_name}')

#Example 2
a=24
b='day'
print(f'there are {a}in {b}')



