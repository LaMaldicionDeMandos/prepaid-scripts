from practice import Practice
from practice_codes_loader import PracticeCodeLoader
from excel_loader import ExcelLoader
import env_file
import sys
from pymongo import MongoClient
from bson.objectid import ObjectId

ENV = env_file.get(path='.env-' + sys.argv[1])

mongoClient = MongoClient(ENV['MONGO_URL'])

db = mongoClient.prepaid

practice_collenction = db.practices


def find_practice(p_name, codes):
    for pr in codes:
        if pr.name.strip() == p_name.strip():
            return pr
    return None


def map_practice_to_mongo(pr):
    mongo_practice = pr.to_dic()
    mongo_practice['_id'] = str(ObjectId())
    return mongo_practice


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

for practice in practices:
    print(practice.to_json())

practice_collenction.insert_many(map(map_practice_to_mongo, practices))
