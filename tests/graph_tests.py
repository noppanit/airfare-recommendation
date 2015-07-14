from tests.helpers.graph_test_context import GraphTestContext
from airfare.atc import *

class GraphTests(GraphTestContext):

    def test_create_city(self):
        create_unique_city('1', 'New York')

        city = find_city('1')
        self.assertEquals('1', city['city_id'])
        self.assertEquals('New York', city['name'])
    
    def test_create_multiple_cities(self):
        create_unique_city('2', 'New York')
        create_unique_city('2', 'New York')

        city = find_city('2')
        self.assertEquals('2', city['city_id'])
        self.assertEquals('New York', city['name'])
        
    def test_create_relationship(self):
        newyork = create_unique_city('1', 'New York')
        boston = create_unique_city('2', 'Boston')

        create_flight_details(fm=newyork, to=boston, miles=1000, fare=100)

        fm, routes = find_routes('1')
        route = routes[0]

        self.assertEquals('1', fm['city_id'])
        self.assertEquals('New York', fm['name'])
        self.assertEquals(100, route['destination']['fare'])
        self.assertEquals(1000, route['destination']['miles'])

    def test_get_cities(self):
        newyork = create_unique_city('1', 'New York')
        boston = create_unique_city('2', 'Boston')

        cities = find_cities()
        actual_newyork = cities[0]
        actual_boston = cities[1]

        self.assertEquals(2, len(cities))

        self.assertEquals('1', actual_newyork['city_id'])
        self.assertEquals('New York', actual_newyork['name'])
        self.assertEquals('2', actual_boston['city_id'])
        self.assertEquals('Boston', actual_boston['name'])


        
        
        
        

