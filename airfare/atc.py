from py2neo import Graph, Path, Relationship

import csv
import os

graph = Graph('http://neo4j:neo4j@localhost:7474/db/data/')

def find_city(city_id):
    results = graph.cypher.execute("MATCH (city:City {city_id: '%s'} ) RETURN city" % city_id)
    if len(results) >= 1:
        return results[0]['city']

def create_unique_city(city_id, city_name):
    found_city = find_city(city_id)
    if found_city:
        return found_city

    cypher = 'CREATE (city:City { city_id: "%s", name: "%s" }) RETURN city' % (city_id, city_name)
    return graph.cypher.execute(cypher)[0]['city']

def delete_all(env=os.environ):
    graph.cypher.execute('MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r')

def create_flight_details(fm, to, miles, fare, year, quarter):
    from_city_to_city = Relationship(fm, "FLY", to, miles=miles, fare=fare, year=year, quarter=quarter)
    graph.create(from_city_to_city)

def find_routes(city_id):
    results = graph.cypher.execute("MATCH (city {city_id: '%s'} )-[r]->(to_city) WHERE r.year = '2014' and r.quarter = '1' RETURN r" % city_id)
    routes = [result['r'] for result in results]
    
    if len(routes) > 0:
        start_node = routes[0].start_node
        fm = {'city_id': start_node['city_id'], 'name': start_node['name']}
        
        return fm, [{'destination': {'city_id': route.end_node['city_id'], 'name': route.end_node['name'], 'miles': route['miles'], 'fare': route['fare'], 'year': route['year'], 'quarter': route['quarter']} } for route in routes]
    
    return None

def find_cities():
    results = graph.cypher.execute('START city=node(*) RETURN city')
    cities = [result['city'] for result in results]
    return [{'city_id': city['city_id'], 'name': city['name']} for city in cities]

    
