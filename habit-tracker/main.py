# Link to Tracker - https://pixe.la/v1/users/ayushn/graphs/graph1.html
import requests
import datetime

USERNAME = "ayushn"
TOKEN = ""
GRAPH_ID = "graph1"
TODAY = datetime.datetime.now()
YESTERDAY = datetime.datetime(year=2024, month=6, day=24)

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {"token": TOKEN,
               "username": USERNAME,
               "agreeTermsOfService": "yes",
               "notMinor": "yes",
               }

# # Creating new account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {"id": GRAPH_ID,
                "name": "Programming-Graph",
                "unit": "hours",
                "type": "float",
                "color": "ajisai",
                }

headers = {
    "X-USER-TOKEN": TOKEN
           }

# # Create a Graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_params = {"date": TODAY.strftime("%Y%m%d"),
                "quantity": input("How many hours did you do programming today? ")}

# # Create a Pixel
response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{YESTERDAY.strftime('%Y%m%d')}"
update_pixel_params = {
    "quantity": "1",
                       }

# # Update a pixel
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{YESTERDAY.strftime('%Y%m%d')}"

# # Delete a pixel
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
