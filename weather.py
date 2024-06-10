import requests

api_key = "de813b00c655b51d656811e5394737d2"

city = input("Where would you like to see the weather for?")

url = (f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

response = requests.get(url)
if response.status.code == 200