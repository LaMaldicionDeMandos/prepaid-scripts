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


def sanitize_list(x):
    y = x.replace('”', '"').replace('“', '"').replace('", "', '","').split('","')
    return list(map(lambda v: v.replace('"', '').strip(), y))

entities = []
for row in rows:
    entity_type = row[1].value
    if entity_type is not None:
        business_name = row[2].value
        fantasy_name = row[3].value
        last_name = row[4].value
        first_name = row[5].value
        enrollment = row[6].value
        specialties = sanitize_list(row[7].value)
        practices = sanitize_list(row[8].value)
        province = row[9].value
        city = row[10].value
        town = row[11].value
        address_street = row[12].value
        address_number = int(row[13].value) if row[13].value is not None else None
        address_floor = row[14].value
        address_flat = row[15].value
        phone = str(int(row[16].value)) if row[16].value is not None else None
        email = row[17].value
        entity = HealthEntity(entity_type, business_name, fantasy_name, last_name, first_name, enrollment, specialties,
                              practices, province, city, town, address_street, address_number, address_floor,
                              address_flat, phone, email)
        entities.append(entity)
        print(entity.to_dic())

customers_collenction.insert_many(map(map_customer_to_mongo, entities))
