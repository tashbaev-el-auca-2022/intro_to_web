import requests

api_url = "https://api.example.com/weather"

params = {
    "city":"Bishkek",
    "your_api_key":"your_api_key"
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    weather = response.json()
    print("Current weather data:")
    print(weather)
else:
    print("Failed to retrieve data. Status code:", response.status_code)