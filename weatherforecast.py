api_key = "18a6aa9fb9dda14a3d31836e84eced7f"
web = "http://api.openweathermap.org/data/2.5/weather?"
import numpy as np
import requests, json
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
def forecast():
    api_key = "18a6aa9fb9dda14a3d31836e84eced7f"
    web = "http://api.openweathermap.org/data/2.5/weather?"
    print('WEATHER FORECAST SERVICES')
    city_name = input("Enter city name : ") 
    URL = web + "appid=" + api_key + "&q=" + city_name 
    data = requests.get(URL)
    out = data.json() 
    if  data.status_code == 200:
        allin = out["main"]
        temperature = allin["temp"] 
        weather = out["weather"]
        weather1 = weather[0]['main']
        weather2 = weather[0]['description']
        current_humidity = allin["humidity"]
        coords = out['coord']
        long = coords['lon']
        lat = coords['lat']
        wind = out['wind']['speed']
        degree_sign = u"\N{DEGREE SIGN}"
        print(f"Welcome to '{(city_name).upper()}'")
        print(f"|  Geo. coords in long/lat : \n|  Longitude : {long} || Latitude : {lat}")
        print("-"*50)
        print(f"|  Current Temperature : {(round(((temperature)-273.15),2))}{degree_sign} C\n|  Current Humidity : {current_humidity} %")
        print(f"|  Weather Condition currently : {weather1}\n|  Weather Condition status : {(weather2).title()}\n|  Wind speed : {wind} km/h")
        
    elif data.status_code >200:
        print("Come on man, be serious !")
        print("\n"*2)
    breturn forecast()


print(forecast())
