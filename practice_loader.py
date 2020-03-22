from practice import Practice
from practice_codes_loader import PracticeCodeLoader
from excel_loader import ExcelLoader
import env_file
import sys

ENV = env_file.get(path='.env-' + sys.argv[1])


def find_practice(p_name, codes):
    for pr in codes:
        if pr.name == p_name:
            return pr
    return None


practice_codes = PracticeCodeLoader(ENV['NOMENCLATOR']).practices
practiceLoader = ExcelLoader(ENV['BASE'])

ws = practiceLoader.sheet('ARBOL')

rows = list(ws.iter_rows())[1:]

practices = []
for row in rows:
    super_type = row[0].value if row[0].value else super_type
    type = row[1].value if row[1].value else type
    name = row[2].value
    practice_code = find_practice(name, practice_codes)
    if practice_code is None:
        print("No encontre " + name)
    else:
        practice = Practice(practice_code.code, practice_code.module, name, type, super_type, practice_code.price)
        practices.append(practice)
"""
print()
print("Comienzo a imprimir las practicas")
for practice in practices:
    print(practice.to_json())
"""

