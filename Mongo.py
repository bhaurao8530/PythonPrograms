import pymongo
client = pymongo.MonogoClient('mongodb://localhost:27017/')
db = client['mydb']
mycol = db["employee"]
print(db.list_collection_names())