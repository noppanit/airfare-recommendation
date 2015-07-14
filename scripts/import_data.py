import sys
import os.path
parent = os.path.abspath(os.path.join(os.path.dirname(__file__),'..')) 
sys.path.append(parent)

from airfare.atc import create_unique_city, create_flight_details

import csv

with open('data/domestic-flights.csv', 'rt') as csv_file:
    routes = csv.reader(csv_file)

    for idx, route in enumerate(routes):
        if idx != 0:
            from_city_id_1 = route[4]
            to_city_id_1 = route[5]

            from_city = route[6]
            to_city = route[7]
            miles = route[8]
            fare = route[10]

            from_node = create_unique_city(from_city_id_1, from_city)
            to_node = create_unique_city(to_city_id_1, to_city)

            create_flight_details(fm=from_node, to=to_node, miles=miles, fare=fare)

