from practice import PracticeCode
from excel_loader import ExcelLoader


class PracticeCodeLoader:
    def __init__(self, file_path):
        self.practices = []
        practice_loader = ExcelLoader(file_path)

        rows = list(practice_loader.sheets()[1].rows)[1:]
        for row in rows:
            if row[0].value is not None:
                practice = PracticeCode(row[0].value, row[1].value, round(row[2].value, 2) if row[2].data_type == 'n' and row[2].value is not None else None)
                self.practices.append(practice)

        rows = list(practice_loader.sheets()[2].rows)
        for row in rows:
            if row[0].value is not None:
                practice = PracticeCode(row[0].value, row[1].value.upper(), round(row[3].value, 2) if row[3].data_type == 'n' and row[3].value is not None else None)
                self.practices.append(practice)
