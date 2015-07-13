from py2neo import Graph, Path, Relationship
graph = Graph('http://neo4j:b4402695@localhost:7474/db/data/')

results = graph.cypher.execute("MATCH (city {city_id: '31703'} )-[r]-(to_city) RETURN r")

print(results)


