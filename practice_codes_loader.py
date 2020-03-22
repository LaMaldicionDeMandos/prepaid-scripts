from practice import PracticeCode
from excel_loader import ExcelLoader


class PracticeCodeLoader:
    def __init__(self, file_path):
        self.practices = []
        practice_loader = ExcelLoader(file_path)
        rows = list(practice_loader.sheets()[0].rows)[7:]
        for row in rows:
            if row[0].value is not None:
                practice = PracticeCode(str(int(row[1].value)), str(int(row[0].value)), row[2].value, round(row[3].value, 2))
                self.practices.append(practice)
