# import requests

# url = "https://api.open-meteo.com/v1/forecast?latitude=31.5204&longitude=74.3587&current_weather=true"

# response = requests.get(url)
# data = response.json()

# print(data)











# import requests

# url = "https://api.open-meteo.com/v1/forecast?latitude=31.5204&longitude=74.3587&current_weather=true"

# response = requests.get(url)
# data = response.json()

# weather = data["current_weather"]

# print("Temperature:", weather["temperature"])
# print("Wind Speed:", weather["windspeed"])




import requests

city_lat = input("Enter latitude: ")
city_lon = input("Enter longitude: ")

url = f"https://api.open-meteo.com/v1/forecast?latitude={city_lat}&longitude={city_lon}&current_weather=true"

response = requests.get(url)
data = response.json()

weather = data["current_weather"]

print("Temperature:", weather["temperature"])
print("Wind Speed:", weather["windspeed"])