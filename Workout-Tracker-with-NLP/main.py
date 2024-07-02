import requests
import datetime as dt

NUTRITION_API_KEY = "9b3ab7e66f3f2fdee9e010d20d01968c"
NUTRITION_APP_ID = "fd0011fa"
BEARER_KEY = "apiowtenfpoinfkagnerwipn"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/1d1c5022df0878a9cf4f9b75bd5eac15/workoutTracker/workouts"

headers = {"x-app-id": NUTRITION_APP_ID,
           "x-app-key": NUTRITION_API_KEY}

query = input("What exercise did you do? ")
exercise_params = {"query": query}

workout_response = requests.post(url=nutritionix_endpoint, json=exercise_params, headers=headers)
exercises = workout_response.json()['exercises']

date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%H:%M:%S")

# sheety_response = requests.get(url=sheety_endpoint)
# print(sheety_response.json())

headers = {"Authorization": f"Bearer {BEARER_KEY}"}

for exercise in exercises:
    workout_parameters = {'workout': {"date": date,
                                      "time": time,
                                      "exercise": exercise['name'],
                                      "duration": exercise['duration_min'],
                                      "calories": exercise['nf_calories'],
                                      }
                          }

    sheety_response = requests.post(url=sheety_endpoint, json=workout_parameters, headers=headers)
    print(sheety_response.text)
