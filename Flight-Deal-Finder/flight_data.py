class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(flights):
    if flights is None or not flights['data']:
        print("No Flight Data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = flights['data'][0]
    lowest_price = float(first_flight['price']['grandTotal'])
    origin = first_flight['itineraries'][0]['segments'][0]['departure']['iataCode']
    destination = first_flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
    out_date = first_flight['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
    return_date = first_flight['itineraries'][1]['segments'][0]['departure']['at'].split('T')[0]

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    for flight in flights['data'][0]:
        price = float(first_flight['price']['grandTotal'])
        if price < lowest_price:
            lowest_price = float(first_flight['price']['grandTotal'])
            origin = first_flight['itineraries'][0]['segments'][0]['departure']['iataCode']
            destination = first_flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
            out_date = first_flight['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
            return_date = first_flight['itineraries'][1]['segments'][0]['departure']['at'].split('T')[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest Price to {destination} is ${lowest_price}")

    return cheapest_flight