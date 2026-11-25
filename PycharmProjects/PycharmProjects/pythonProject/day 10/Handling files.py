# 1 To open and write in the file
# file=open("D:\Selenium\demofiles.txt",'w')   #location of file and write
# file.write("This is my First statement.....\n") #\n for next line
# file.write("This is my second statement.....\n")
# file.write("This is my third statement.....\n")
# file.write("This is my Fourth statement.....\n")
# file.write("This is my Fifth statement.....\n")
# file.close()
# print("Program completed")

#2 To read the file
file=open("D:\Selenium\demofiles.txt",'r')
print(file.read())
#print(file.readline())
#print(file.readlines())
# file.close()
# print("Program is completed")

#3 appending data into text file

file=open("D:\Selenium\demofiles.txt",'a')
file.write("\n this is 6th line..\n")
file.write("\n this is 7th line..\n")
file.close()
print("Program is completed")
