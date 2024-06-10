import requests
import math
from configparser import ConfigParser
import tkinter as tk
from tkinter import messagebox

# Setting up the main window for the application
root = tk.Tk() # Creates the main window
root.title("Python Weather App") #Setting window title
root.geometry("300x200") # Setting window dimensions

city_label = tk.Label(root, text="Enter City:") # label for the city input
city_label.pack(pady=10) # adding the label to the window with padding

city_entry = tk.Entry(root) # Creating an entry widget for user input
city_entry.pack(pady=5) # Adding the entry widget to the window padding

# Read the API key from the config file
config = ConfigParser()
config.read('config.cfg')
api_key = config.get('api_keys','api_key')

# Prompt the user to enter the city for which they want to see the weather
city = input("Where would you like to see the weather for?")

# Create the URL for the weather API request
url = (f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

# Send the API request and get the response
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()
    
    # Extract the temperature and description from the data
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    
    # Print the temperature in Celsius and the weather description
    print(f"Temperature: {math.floor(temp - 273.15)} C")
    print(f"Description: {desc}")
else: 
    # Print an error message if the request was not successful
    print('Error fetching weather data')
    print(f'status code: {response.status_code}')