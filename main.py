import requests
import os
from dotenv import find_dotenv, load_dotenv
import datetime


# ----------------------------------------------------------------------------------------------------------------------
# ---------------- #
#  Dotenv set up   #
# ---------------- #

# Find the .env file on the directory and then load the file to be used
dot_env_file = find_dotenv()
load_dotenv(dot_env_file)

# ----------------------------------------------------------------------------------------------------------------------
# ---------------- #
#    CONSTANTS     #
# ---------------- #

# My information
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

# My account NutritionixAPI credentials (https://www.nutritionix.com/business/api)
APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

# API Natural language for exercise endpoint  (https://docx.syndigo.com/developers/docs/natural-language-for-exercise)
WORKOUT_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


# Sheety API authentication (https://sheety.co/docs/requests.html)
TOKEN = os.getenv("TOKEN")
SHEET_ENDPOINT = "https://api.sheety.co/36c7b6595414d1f2e43ab86dbc510f28/workoutTracking/workouts"


# ----------------------------------------------------------------------------------------------------------------------
# -------------------- #
#  workout api set up  #
# -------------------- #

# The text input for the exercise to be passed on as the 'query' key for the request
exercise_input = input("Tell me what exercise you did: ")

# Headers for authentication for the API using the APP key & id for my account
workout_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

# Parameters to pass on to the request. (Query is the only required key)
params = {
    "query": exercise_input,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# The POST request to retrieve the data
response = requests.post(url=WORKOUT_ENDPOINT, json=params, headers=workout_headers)
response.raise_for_status()
result = response.json()

# ----------------------------------------------------------------------------------------------------------------------
# ------------------- #
#  Sheety api set up  #
# ------------------- #

# Use the datetime and format the date (dd/mm/yyyy) and the current time (hh/mm/ss) to be passed to the Google sheet
# to indicate the date of exercise entry
now = datetime.datetime.now()
today_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%X")

# Headers for authentication to use the Google sheet
sheet_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

# This for loop creates a sheet_input(basically parameters for the Google sheet) to be passed in the POST request
# and create a new row in the Google sheet.
"""
In case, there are multiple types of exercises inputed in the same query by the user this would create a list of 
different dictionaries for each type of exercise in the input.

To avoid just taking one exercise if there are multiple the for loop goes trough the results 'exercises' key creating
a sheet_input to be passed in the post reqeust to update the sheet.

"workout" key is named so due to the endpoint for the sheet having that name (https://sheety.co/docs/requests.html)

all the other keys are headers that are in the google sheet so the API knows where to populate what data.
and all the values are simpli data extracted from the workout results per exercise.
"""
for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # For each exercise, create a POST request to create a row in the Google sheet
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_input, headers=sheet_headers)

    # Print for testing purposes
    print(sheet_response.text)
