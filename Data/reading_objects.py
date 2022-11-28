import xlrd
from Library.config import Config

class LBehave:
    def read_data(self,sheetname):
        workbook = xlrd.open_workbook(Config.Path)
        worksheet = workbook.sheet_by_name(sheetname)
        col = worksheet.ncols
        row = worksheet.get_rows()
        header = next(row)
        data=[]
        for item in row:
            values = ()
            for j in range(col):
                values += (item[j].value,)
            data.append(values)
        return data


    def read_locators(self,sheetname):
        workbook = xlrd.open_workbook(Config.Path)
        worksheet=workbook.sheet_by_name("Jewelry")
        rows=worksheet.nrows
        print(rows)
        d={}
        for i in range(rows):
            row=worksheet.row_values(i)
            d[row[0]]=(row[1],row[2])
        return d