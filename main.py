import requests

OWM_Endpoint = "https://api.weatherapi.com/v1/forecast.json"
api_key = "a7df46d9b8b7442e826192717242006"
MY_LAT = 23.034161
MY_LAN = 72.548492


weather_param = {
    "key": api_key,
    "q": f"{MY_LAT},{MY_LAN}"
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_param)
weather_Data = response.json()
weather_slice = weather_Data["forecast"]["forecastday"][0]["hour"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["condition"]["code"]
    if int(condition_code) >= 1063:
        print("Bring an Umbrella")