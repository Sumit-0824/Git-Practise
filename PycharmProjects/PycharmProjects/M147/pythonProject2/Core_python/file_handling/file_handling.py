# file :it is container which is used to store the data.
# File Handling: it is a process of writing the data into the file or reading the
# data from the file
# open():
# without context manager
# var_name = open(file_name.ext,mode)
# ..
# var_name.close()

# with context manager
# with open(file_name.ext,mode) as file_obj/var_name:
#       statement block

# mode = 'w','r','a'

# write data to file
# var_name.write()
# var_name.writelines()

f=open(r'sample.txt','w')
f.write('Hi you are writing the data into sample \n')
f.writelines(['Hi Sumit, This is file handling class \n','this is writelines function\n'])
f.close()

f1=open(r'sample.txt','a')
f1.write('End of lines \n')
f1.close()

# to find the path
#import os
#os.getcwd()
#'C:\\Users\\Sumit\\PycharmProjects\\M147\\pythonProject2'
#If wanted in different directory
#f=open(r'C:\\Users\\Sumit\\PycharmProjects\\M147\\{project name}\\sample.txt','w')

# read
# var_name.read()
# var_name.readline()
# var_name.readlines()

'''
If file in same folder
with open(r'sample_file.txt','r') as f:

    for i in f:
        print(i.strip())
'''

#if file in different folder
with open(r'C:\Users\Sumit\Desktop\Qspider python classes\Files\sample_file.txt','r') as f:
    for i in f:
        print(i.strip())

'''
output
Strings
Lists
Tuples
Dictionaries
Comprehensions (List and Dictionary)
Functions
Decorators
Custom Sorting
Booleans
Unpacking
'''

#in index and value pair
with open(r'C:\Users\Sumit\Desktop\Qspider python classes\Files\sample_file.txt','r') as f1:
    for num,value in enumerate(f1,start=1):
        print(num,value.strip())
#Output
'''

1 Strings
2 Lists
3 Tuples
4 Dictionaries
5 Comprehensions (List and Dictionary)
6 Functions
7 Decorators
8 Custom Sorting
9 Booleans
10 Unpacking

'''
#in dictionary
with open(r'C:\Users\Sumit\Desktop\Qspider python classes\Files\sample_file.txt','r') as f2:
    d={}
    for num, value in enumerate(f2, start=1):
        d[num]=value.strip()
print(d)
#Output-{1: 'Strings', 2: 'Lists', 3: 'Tuples', 4: 'Dictionaries', 5: 'Comprehensions (List and Dictionary)', 6: 'Functions', 7: 'Decorators', 8: 'Custom Sorting', 9: 'Booleans', 10: 'Unpacking'}


d = {'67.218.116.165': 2, '66.249.71.65': 3, '65.55.106.183': 2, '66.249.65.12': 32, '65.55.106.131': 2, '08:06': 1, '65.55.106.186': 1, '74.52.245.146': 2, '66.249.65.43': 3, '65.55.207.25': 2, '65.55.207.94': 2, '65.55.207.71': 1, '98.242.170.241': 1, '66.249.65.38': 100, '65.55.207.126': 2, '82.34.9.20': 2, '65.55.106.155': 2, '65.55.207.77': 2, '208.80.193.28': 1, '89.248.172.58': 22, '67.195.112.35': 16, '65.55.207.50': 3, '65.55.215.75': 2}

#f={ip:d.count(ip)for ip in d}
#print(sorted(d.items(),key=lambda i:i[1]))


d = {
    '67.218.116.165': 2, '66.249.71.65': 3, '65.55.106.183': 2, '66.249.65.12': 32,
    '65.55.106.131': 2, '08:06': 1, '65.55.106.186': 1, '74.52.245.146': 2,
    '66.249.65.43': 3, '65.55.207.25': 2, '65.55.207.94': 2, '65.55.207.71': 1,
    '98.242.170.241': 1, '66.249.65.38': 100, '65.55.207.126': 2, '82.34.9.20': 2,
    '65.55.106.155': 2, '65.55.207.77': 2, '208.80.193.28': 1, '89.248.172.58': 22,
    '67.195.112.35': 16, '65.55.207.50': 3, '65.55.215.75': 2
}

# Sort the dictionary by value (frequency of the IP or key) using lambda
sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)

# Get the maximum frequency value
max_count = sorted_d[0][1]     #sorted_d[0]=====('66.249.65.38', 100)

print(f"Maximum count of records: {max_count}")
#('66.249.65.38', 100)
#Maximum count of records: 100

####2################
def read_txt():
    records=[]
    with open(r'C:\Users\Sumit\Desktop\Qspider python classes\Files\sample.log','r') as obj:
        for line in obj:
            clean_line=line.strip()
            if clean_line:
                words=clean_line.split()[0]
                records.append(words)
    return records
print(read_txt())
