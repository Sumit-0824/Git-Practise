# ---------------------------------------------------------------------------------
string = "Hi Welcome to python"
# # 1. Print Even index Characters of string.
print(string[::2])                                        #o/p---> H ecm opto
# # 2. Print Every Alternate Characters in reverse order
print(string[::-2])                                       #o/p--->nhy teolWi
# # 3. Print the string in reversed order
rev_str= string[::-1]                                     #0/p--->nohtyp ot emocleW iH
print(rev_str)

# # 4. Print extension of the filename
a = 'Youtube.txt'                                          #o/p---->txt
print(a[8::1])     #or print(a[-3::])
# # 5. Print only filename
print(a[0:7:1])    #print(a[0:-4:1)                                        #o/p------>Youtube
# # 6. Printing only protocol in
url = 'https://google.com'
print(url[0:5:1])                                           #o/p------>https