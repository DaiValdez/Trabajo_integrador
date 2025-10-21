from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["viajes_db"]

def test_connection():
    print("Bases disponibles:", client.list_database_names())
    
