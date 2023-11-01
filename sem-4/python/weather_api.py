#api-key=7bdccf825b7dd119a05ac2e0afaf1aaa

import requests, json
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = input("Enter City name : ")
API_KEY = input("Enter your API_KEY : ")
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL)

if response.status_code == 200:
 data = response.json()
 main = data['main']
 temperature = main['temp']
 humidity = main['humidity']
 pressure = main['pressure']
 report = data['weather']
 print(f"{CITY:}")
 print(f"Temperature: {temperature}")
 print(f"Humidity: {humidity}")
 print(f"Pressure: {pressure}")
 print(f"Weather Report: {report[0]['description']}")
else:
 print("Error in the HTTP request")
