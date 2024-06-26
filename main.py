import requests
import os
from dotenv import find_dotenv, load_dotenv


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

# My account NutritionixAPI credentials (https://www.nutritionix.com/business/api)
APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY_KEY")

# API Natural language for exercise endpoint  (https://docx.syndigo.com/developers/docs/natural-language-for-exercise)
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Headers for authentication for the API using the APP key & id for my account
HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

# ----------------------------------------------------------------------------------------------------------------------
# ---------------- #
#  Program set-up  #
# ---------------- #
