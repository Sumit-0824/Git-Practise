#Reading the file
import openpyxl

#file-->Workbook-->Sheets-->Rows-->Cells
file="C:\\Users\\Sumit\\Downloads\\Sumit\\Selenium\\data2.xlsx"
workbook=openpyxl.load_workbook(file)
sheet=workbook.active   #sheet=Workbook["Data"]
#rows=sheet.max_row #count number of rows in a excel
#cols=sheet.max_column #count number of cols in a excel

#Reading all the rows &column from excel
sheet.cell(1,1).value ="Sumit"
sheet.cell(1,2).value = '1992'
sheet.cell(1,3).value ="Bangalore"

sheet.cell(2,1).value ="Prerna"
sheet.cell(2,2).value = '1989'
sheet.cell(2,3).value ="Jamui"

sheet.cell(3,1).value ="Ankit"
sheet.cell(3,2).value = '1995'
sheet.cell(3,3).value ="Patna"


workbook.save(file)