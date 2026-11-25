import openpyxl
from openpyxl.styles import PatternFill

def getRowCount(file,SheetName):
    workbook=openpyxl.load_workbook(file)
    Sheet=workbook[SheetName]
    return(Sheet.max_row)

def getRowCount(file,SheetName):
    workbook=openpyxl.load_workbook(file)
    Sheet=workbook[SheetName]
    return(Sheet.max_column)

def readData(file,SheetName,rownum,columnno):
    workbook = openpyxl.load_workbook(file)
    Sheet = workbook[SheetName]
    return Sheet.cell(rownum,columnno).value

def WriteData(file,SheetName,rownum,columnno,data):
    workbook = openpyxl.load_workbook(file)
    Sheet = workbook[SheetName]
    Sheet.cell(rownum,columnno).value= data
    workbook.save(file)


def fillGreencolor(file,SheetName,rownum,columnno):
    workbook = openpyxl.load_workbook(file)
    Sheet = workbook[SheetName]
    greenFill =PatternFill(start_color='60b212',
                           end_color='60b212',
                           fill_type='solid')
    Sheet.cell(rownum,columnno).fill=greenFill
    workbook.save(file)


def fillRedcolor(file,SheetName,rownum,columnno):
    workbook = openpyxl.load_workbook(file)
    Sheet = workbook[SheetName]
    redFill =PatternFill(start_color='ff0000',
                           end_color='ff0000',
                           fill_type='solid')
    Sheet.cell(rownum,columnno).fill=redFill
    workbook.save(file)





