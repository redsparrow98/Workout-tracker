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


# ----------------------------------------------------------------------------------------------------------------------
# -------------------- #
#  workout api set up  #
# -------------------- #


# The text input for the exercise to be passed on as the 'query' key for the request
# exercise_input = input("Tell me what exercise you did: ")

# Headers for authentication for the API using the APP key & id for my account
headers = {
    'Content-Type': 'application/json',
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

# # The POST request to retrieve the data
# response = requests.post(url=WORKOUT_ENDPOINT, json=params, headers=headers)
# response.raise_for_status()
# result = response.json()
# print(result)


# ----------------------------------------------------------------------------------------------------------------------
# ------------------- #
#  Sheety api set up  #
# ------------------- #

# Use the datetime and format the date (dd/mm/yyyy) to be passed to the Google sheet to indicate the date of
# exercise entry
now = datetime.datetime.now()
formatted_date = now.strftime("%d/%m/%Y")
