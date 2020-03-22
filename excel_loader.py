from openpyxl import load_workbook


class ExcelLoader:
    def __init__(self, file_path):
        self.__wb = load_workbook(filename=file_path, read_only=True)

    def sheet(self, sheet_name):
        return self.__wb.get_sheet_by_name(sheet_name)

    def sheets(self):
        return self.__wb.worksheets
