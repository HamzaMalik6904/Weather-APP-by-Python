import requests
import json
city=input("Enter the name of the city\n")
url=f"http://api.weatherapi.com/v1/current.json?key=dc33f0ef98c7404fae2112917250202&q={city}"
r=requests.get(url)
# print(r.text)
wdic=json.loads(r.text)
print(f"The Temprature in {city }")
print(wdic["current"]["temp_c"])

print(f"The Weather condition in {city }")
print(wdic["current"]["condition"]["text"])