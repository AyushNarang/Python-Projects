import requests
import os
from dotenv import load_dotenv

load_dotenv()


class FlightSearch:
    def __init__(self):
        self.amadeus_token_endpoint = f"{os.getenv('amadeus_endpoint')}/security/oauth2/token"
        self.amadeus_city_endpoint = f"{os.getenv('amadeus_endpoint')}/reference-data/locations/cities"
        self.amadeus_flight_endpoint = f"https://test.api.amadeus.com/v2/shopping/flight-offers"
        self._api_key = os.getenv('AMADEUS_API_KEY')
        self._api_secret = os.getenv('AMADEUS_API_SECRET')
        self._token = self._get_new_token()

    def send_iata(self, city):
        amadeus_params = {"keyword": city,
                          "max": 2,
                          "include": "AIRPORTS",
                          }
        headers = {"Authorization": f"Bearer {self._token}"}
        amadeus_response = requests.get(url=self.amadeus_city_endpoint, params=amadeus_params, headers=headers)
        try:
            return amadeus_response.json()["data"][0]['iataCode']
        except IndexError:
            return "N/A"
        except KeyError:
            return "Not Found"

    def _get_new_token(self):
        amadeus_header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        amadeus_params = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }
        amadeus_response = requests.post(url=self.amadeus_token_endpoint, data=amadeus_params, headers=amadeus_header)
        return amadeus_response.json()['access_token']

    def flight_search(self, origin_code, dest_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        params = {
            "originLocationCode": origin_code,
            "destinationLocationCode": dest_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "currencyCode": "USD",
            "max": 10,
        }
        response = requests.get(url=self.amadeus_flight_endpoint, params=params, headers=headers)
        if response.status_code != 200:
            print("Error fetching flights.")
            print(response.text)
            return None
        return response.json()
