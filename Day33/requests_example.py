import requests

LONGITUDE = 37.566536
LATITUDE = 126.977966


# response = requests.get("http://api.open-notify.org/is-now.json")
# try:
#     response.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     print(err)
# else:
#     data = response.json()
#     print(data)
#
#     latitude = data['iss_position']['latitude']
#     longitude = data['iss_position']['longitude']
#     iss_position = (latitude, longitude)
#     print(iss_position)


parameter = {
    "lat":LATITUDE,
    "lng":LONGITUDE,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunrise)
print(sunrise_hour)
