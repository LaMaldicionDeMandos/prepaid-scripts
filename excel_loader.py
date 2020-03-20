from openpyxl import load_workbook

class ExcelLoader:
    def __init__(self, filePath):
        self.__wb = load_workbook(filename=filePath, read_only=True)

    def sheet(self, sheetName):
        return self.__wb.get_sheet_by_name(sheetName)
