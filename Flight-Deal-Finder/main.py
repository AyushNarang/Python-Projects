from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
import time
import datetime as dt

ORIGIN_CITY = "MCO"

sheet_obj = DataManager()
sheet_data = sheet_obj.send_data()
pprint(sheet_data)
flight_obj = FlightSearch()

tomorrow = dt.datetime.now() + dt.timedelta(days=1)
six_months_from_today = dt.datetime.now() + dt.timedelta(days=(6*30))

for city in sheet_data:
    if not city['iataCode']:
        iata_code = flight_obj.send_iata(city['city'])
        time.sleep(2)
        city['iataCode'] = iata_code
        sheet_obj.change_row(city)
    flights = flight_obj.flight_search(origin_code=ORIGIN_CITY, dest_code=city['iataCode'], from_time=tomorrow, to_time=six_months_from_today)
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{city['city']}: ${cheapest_flight.price}")
    time.sleep(2)
