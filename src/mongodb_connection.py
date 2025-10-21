# Conecto con MongoDB desde Python
from pymongo import MongoClient

# Función que devuelve el cliente de MongoDB
def get_mongo_client():
    # mongodb://localhost:27017/ -> dirección y puerto que usamos en Docker
    client = MongoClient("mongodb://localhost:27017/")
    return client

# Solo corre si ejecuto este archivo directamente
if __name__ == "__main__":
    client = get_mongo_client()                        # Creo el cliente
    print("MongoDB conectado:", client.list_database_names())  # Muestro las bases de datos existentes
