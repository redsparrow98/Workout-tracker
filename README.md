# Workout Tracker

A simple application that uses Google Sheet and AI to help track your workouts.

Type in the name of the exercise you did as well as the duration, distance, weight used, etc.

Example:
> ran for 5 kilometers and swam for 20 minutes

And the AI will detect the Exercise type and amount of calories or distance and duration based on your
age, height and weight specification for you. The exercises will be saved in the Google Sheet for eas of tracking.

The app is best used on replit allowing you to update your workout sheet on the go.

## Features

- Log workout details such as exercise, sets, reps, and weight.
- Update and view your workout history.
- Simple and intuitive interface.


## Setup
### Prerequisites

- Python 3.8 or higher
- Access to a Google account
- Replit account (optional, for easy deployment)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/redsparrow98/Workout-tracker.git
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```


## Setting up the API's
### API used
1. [NutritionixAPI](https://www.nutritionix.com/business/api)
2. [Sheety](https://sheety.co/)

### NutritionixAPI
1. Go to [NutritionixAPI](https://www.nutritionix.com/business/api)
2. Select Get your API Key
3. Once logged in, you should be able to access your API key and App id
4. For reference to Natural Language for Exercise, use [NutritionixAPI Documentation](https://docx.syndigo.com/developers/docs/nutritionix-api-guide)

### Sheety
1. Go to [Sheety](https://sheety.co/)
2. Log in with your Google account that will have the Google sheet for the workout data
3. Make sure you give Sheety permission to access your Google sheets
4. In your project page, click on "New Project" and create a new project in Sheety with the name "Workout Tracking" and paste in the URL of your own "My Workouts" Google Sheet
5. Click on the workouts API endpoint and enable GET and POST



### Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

- `AGE`: Your age for the calories to be accurate
- `HEIGHT_CM`: Your height in centimeters for the calories to be accurate
- `WEIGHT_KG`: Your weight in kilograms for the calories to be accurate
- `APP_ID`: NutritionixAPI ID you receive once you create your account
- `APP_KEY`: NutritionixAPI KEY you receive once you create your account
- `SHEET_TOKEN`: Token to authenticate yourself on SheetyAPI
- `SHEET_ENDPOINT`: Endpoint to your Sheety project that is linked to the Google sheet you will store the data in


### Deployment on Replit
1. Fork the repository to your own GitHub account
2. Go to [Replit](https://replit.com)
3. Create a new Repl and import your forked repository
4. Add the environment variables in the Replit secrets tab
5. Run the Repl to start logging your workouts on the go.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request.