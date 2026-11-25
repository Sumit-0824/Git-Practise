# SQL connection/ Banckend Connection:
#  if it is required to communicate with database by establishing the connection
#  with python file. than we should make use of backend connectivity or SQL connection

# In is case we are going to use 7 important function to do the required task
# 1. connect():
# - It is a function which is used to establish the connection b/w python file and database file handling.
# - connect function in present inside sqlite3 module..

# 2. cursor():
# - It is function which is used to make the control to get pointed to the particular location in the database.

# 3. execute():
# - It is a function which is used to execute the quarries.

# 4. commit():
# - It is a function which is used save the changes

# 5. close():
# - It is used to close the connection b/w python file and database file.

# 6. fetchall():
# - It is function which is used to fetch all the match records.

# 7. fetchone():
# - This function is used to fetch the first match record from the o/p.

import sqlite3
#insertion
var=sqlite3.connect('abc.db')
var1=var.cursor()

#var1.execute('create table emp(ename char,eid char)')
var1.execute('insert into emp values("A","TYC123")')
var1.execute('insert into emp values("B","TYC124")')
var1.execute('insert into emp values("C","TYC125")')
var1.execute('insert into emp values("D","TYC126")')
var.commit()
var.close()

#Extraction
f=sqlite3.connect('abc.db')
d=f.cursor()
res=d.execute('select * from emp where ename="A"')
#print(res.fetchall())
print(res.fetchone())  #('A', 'TYC123')
f.commit()
f.close()