import requests

MY_APPID = "8ec38d11d1014445778afa446aeb8fa4"
HIS_APPID = "69f04e4613056b159c2761a9d9e664d2"
MY_LONG = 126.977966
MY_LAT = 37.566536
HIS_LONG = -21.817438
HIS_LAT = 64.126518

# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
parameters = {
    "lat": HIS_LAT,
    "lon": HIS_LONG,
    "appid": HIS_APPID,
    "exclude": "current,minutely,daily,alerts"
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
print(response)
print(response.json())
data = response.json()
twelve_hours_data = data["hourly"][0:12]

will_rain = False
#weather_codes = []
for hour_data in twelve_hours_data:
    weather_list = hour_data["weather"]
    #weather_codes.append(weather_list[0]['id'])
    if int(weather_list[0]['id']) < 700:
        will_rain = True

if will_rain:
    print("Need Umbrella.")

"""
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = "AC4c47db37b43742c3a452c35663056e03"
auth_token = "ea3c46230ae98619fa1a56de1f02db38"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+821054548164',
                     to='+821054548164'
                 )

print(message.sid)
"""