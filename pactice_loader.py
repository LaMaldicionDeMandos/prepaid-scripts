from practice import Practice
from excel_loader import ExcelLoader

practiceLoader = ExcelLoader('../Base.xlsx')

ws = practiceLoader.sheet('ARBOL')

rows = list(ws.iter_rows())[1:]

practices = []
i = 1
for row in rows:
    superType = row[0].value if row[0].value else superType
    type = row[1].value if row[1].value else type
    name = row[2].value
    price = round(row[3].value, 2)
    practice = Practice(i, name, type, superType, price)
    i = i + 1
    practices.append(practice)

for practice in practices:
    print(practice.toJson())
