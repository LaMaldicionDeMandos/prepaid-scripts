from excel_loader import ExcelLoader
import env_file
import sys
from pymongo import MongoClient
from bson.objectid import ObjectId
from customer import HealthEntity

ENV = env_file.get(path='.env-' + sys.argv[1])

mongoClient = MongoClient(ENV['MONGO_URL'])

db = mongoClient.prepaid

customers_collenction = db.health_entities

customerLoader = ExcelLoader(ENV['BASE'])

ws = customerLoader.sheet('BASE COMPLETA')

rows = list(ws.iter_rows())[3:]


def map_customer_to_mongo(pr):
    mongo_practice = pr.to_dic()
    mongo_practice['_id'] = str(ObjectId())
    return mongo_practice


def parseList(value):
    return value


entities = []
for row in rows:
    entity_type = row[1].value
    if entity_type is not None:
        business_name = row[2].value
        fantasy_name = row[3].value
        name = row[4].value
        enrollment = row[5].value
        # Las listas de categorias, especialidades y practicas son listas separadas.
        # Lo que si las practicas tienen que estar en la lista de especialidades y las especialidades tienen que estar en las categorias
        categories = parseList(row[6].value)
        specialties = parseList(row[7].value)
        practices = parseList(row[8].value)
        province = row[9].value
        city = row[10].value
        town = row[11].value
        address = row[12].value
        phone = str(int(row[13].value)) if row[13].value is not None else None
        email = row[14].value
        entity = HealthEntity(entity_type, business_name, fantasy_name, name, enrollment, categories, specialties,
                              practices, province, city, town, address, phone, email)
        entities.append(entity)
        print(entity.to_dic())

#customers_collenction.insert_many(map(map_customer_to_mongo, entities))
