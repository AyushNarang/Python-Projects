import os

import requests
from dotenv import load_dotenv

load_dotenv()

BEARER_KEY = os.getenv('BEARER_KEY')
sheety_endpoint = os.getenv('sheety_endpoint')


class DataManager:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {BEARER_KEY}"}
        self.sheety_response = requests.get(url=sheety_endpoint, headers=self.headers)

    def send_data(self):
        return self.sheety_response.json()['prices']

    def change_row(self, city):
        update_sheety_endpoint = f"{sheety_endpoint}/{city['id']}"
        update_params = {
            'price': {
                'iataCode': city['iataCode']
            }
        }
        update_sheety_response = requests.put(url=update_sheety_endpoint, json=update_params, headers=self.headers)
