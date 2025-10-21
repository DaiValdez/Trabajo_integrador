# Conecto con Neo4j desde Python
from neo4j import GraphDatabase

# Función que devuelve el driver de Neo4j
def get_neo4j_driver():
    # bolt://localhost:7687 -> dirección y puerto que usamos en Docker
    # auth=("neo4j", "trabajo_integrador") -> usuario y contraseña que pusimos
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "trabajo_integrador"))
    return driver

# Solo corre si ejecuto este archivo directamente
if __name__ == "__main__":
    driver = get_neo4j_driver()        # Creo el driver
    with driver.session() as session:  # Abro una sesión
        result = session.run("RETURN 'Conectado a Neo4j' AS mensaje")  # Hago una consulta simple
        print([r["mensaje"] for r in result])  # Muestro el resultado
    driver.close()                     # Cierro la conexión
