import requests

from datetime import datetime

api_key = 'f34363674f5467d17caac427151f9cdc'
location = input("ENTER THE CITY NAME :   ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")



print("-------------------------------------------------------------")
print("Weather stats for - {}  ||  {}".format(location.upper(),date_time))
print("-------------------------------------------------------------")

print("current temperature is : {:.2f} deg C".format(temp_city))
print("current weather desc   :",weather_desc)
print("current humidity       :",hmdt, '%')
print("current wind speed     :",wind_spd,'kmph'