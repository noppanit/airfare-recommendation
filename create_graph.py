from py2neo import Graph, Path, Relationship
import csv

graph = Graph('http://neo4j:b4402695@localhost:7474/db/data/')

def find_city(city_id):
    return graph.cypher.execute("MATCH (city:City {city_id: '%s'} ) RETURN city" % city_id)

def create_city(city_id, city_name):
    cypher = 'CREATE (city:City { city_id: "%s", name: "%s" }) RETURN city' % (city_id, city_name)
    return graph.cypher.execute(cypher)

with open('domestic-flights.csv', 'rt') as csv_file:
    routes = csv.reader(csv_file)
    
    for idx, route in enumerate(routes):
        if idx != 0:
            from_city_id_1 = route[4]
            to_city_id_1 = route[5]
        
            from_city = route[6]
            to_city = route[7]
            miles = route[8]
            fare = route[10]
            
            from_node = find_city(from_city_id_1)
            to_node = find_city(to_city_id_1)
            
            if len(from_node) == 0:
                from_node = create_city(from_city_id_1, from_city)[0]['city']
            else:
                from_node = from_node[0]['city']
            
            if len(to_node) == 0:
                to_node = create_city(to_city_id_1, to_city)[0]['city']
            else:
                to_node = to_node[0]['city']
            
            from_city_to_city = Relationship(from_node, "FLY", to_node, miles=miles, fare=fare)
            graph.create(from_city_to_city)
                   



