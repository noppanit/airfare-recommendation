from py2neo import Graph

graph = Graph('http://neo4j:b4402695@localhost:7474/db/data')
graph.cypher.execute('MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r')
