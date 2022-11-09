import requests

MY_APPID = "W"
MY_LONG = 126.977966
MY_LAT = 37.566536

# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": MY_APPID,
    "exclude": "current,minutely,daily,alerts"
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
print(response)
print(response.json())
data = response.json()
twelve_hours_data = data["hourly"][0:12]

will_rain = False
for hour_data in twelve_hours_data:
    weather_list = hour_data["weather"]
    if int(weather_list[0]['id']) < 700:
        will_rain = True

if will_rain:
    print("Need Umbrella.")

