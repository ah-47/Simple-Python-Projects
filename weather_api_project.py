import requests
import json
import os

city = input("Temperature of which city do u want: ")

url = (f"https://api.weatherapi.com/v1/current.json?key"
       f"=50ee08078e1945e797f133929231509&q={city}")

req = requests.get(url)

# print(req.text)

weather_dic = json.loads(req.text) # convert string into dictonries

temp = weather_dic['current']['temp_c']

# print(temp)

temperature = f'Temperature is {temp} degree in your city {city} '


os.system(f'say {temperature}')