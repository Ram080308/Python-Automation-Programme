import openpyexcel

def get_row_count(path,sheetname):
    workbook = openpyexcel.load_workbook(path)
    sheet = workbook[sheetname]
    return (sheet.max_row)

def get_col_count(path,sheetname):
    workbook = openpyexcel.load_workbook(path)
    sheet = workbook[sheetname]
    return (sheet.max_column)

def data_from_excel(path,sheetname,rownum,colnum):
    workbook = openpyexcel.load_workbook(path)
    sheet = workbook[sheetname]
    return sheet.cell(row=rownum,column=colnum).value

def write_data_to_excel(path,sheetname,rownum,colnum,data):
    workbook = openpyexcel.load_workbook(path)
    sheet = workbook[sheetname]
    sheet.cell(row=rownum, column=colnum).value=data
