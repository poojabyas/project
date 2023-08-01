import requests
import math

apikey = "a53c53f4fa3972e2e0950f287ba24897"

cityname = input("Enter the city name:")
url =  f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&APPID={apikey}"

response = requests.get(url)
data = response.json()
temprature = int(data["main"]["temp"])
temprature = math.ceil(temprature - 273.15)
print(f"The Temprature in {cityname} is {temprature}{chr(176)}C")


# print(data)

# print("current temprature ",data["main"]["temp"])
