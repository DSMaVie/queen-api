from pymongo import MongoClient


cli = MongoClient("mongodb://root:example@localhost:27017")

print(cli["test"]["test_coll"].insert_one({"this": "wow"}).inserted_id)
