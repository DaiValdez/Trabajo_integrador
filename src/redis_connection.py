# Conecto con Redis desde Python
import redis

# Función que devuelve el cliente de Redis
def get_redis_client():
    # localhost = mi PC, 6379 = puerto que configuré en Docker
    client = redis.Redis(host='localhost', port=6379)
    return client

# Solo corre si ejecuto este archivo directamente
if __name__ == "__main__":
    r = get_redis_client()           # Creo el cliente
    r.set("test_key", "hola redis")  # Guardo un valor
    print("Redis dice:", r.get("test_key"))  # Lo muestro
