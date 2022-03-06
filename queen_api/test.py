from pymongo import MongoClient


cli = MongoClient("mongodb://localhost:27017/")
print(cli.ServerInfo)
print(cli.list_databases())
