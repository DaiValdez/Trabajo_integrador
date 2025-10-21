from neo4j import GraphDatabase

uri = "neo4j://127.0.0.1:7687"
user = "neo4j"
password = "trabajo_integrador"

driver = GraphDatabase.driver(uri, auth=(user, password))

def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Conexión exitosa con Neo4j' AS mensaje")
        print(result.single()["mensaje"])
