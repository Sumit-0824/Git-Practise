#Reading the file
import openpyxl

#file-->Workbook-->Sheets-->Rows-->Cells
file="C:\\Users\\Sumit\\Downloads\\Sumit\\Selenium\\data.xlsx"
Workbook=openpyxl.load_workbook(file)
sheet=Workbook["Sheet1"]
rows=sheet.max_row #count number of rows in a excel
cols=sheet.max_column #count number of cols in a excel

#Reading all the rows &column from excel
for r in range(1,rows+1):
    for c in range(1,cols+1):
        print(sheet.cell(r,c).value, end='  ')
    print()
