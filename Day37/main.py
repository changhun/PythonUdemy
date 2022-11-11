import requests
from datetime import datetime, timedelta

API_ENDPOINT = "https://pixe.la/v1/users"
USER = "changhun"
TOKEN = ""


create_user_params = {
    "token": TOKEN,
    "username": "changhun",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(API_ENDPOINT, json=create_user_params)
# print(response)
# print(response.text)

# response = requests.get(f"https://pixe.la/@{USER}")
# response.raise_for_status()
# print(response)
# data = response.json()
# print(data)

POST_API_ENDPOINT = f"https://pixe.la/v1/users/{USER}/graphs"
header = {
    "X-USER-TOKEN": TOKEN
}

params = {
    "id": "graph1",
    "name": "my Graph1",
    "unit": "km",
    "type": "float",
    "color": "sora"
}

# response = requests.post(POST_API_ENDPOINT, json=params, headers=header)
# print(response.text)
     

# POST PIXEL
# https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5","optionalData":"{\"key\":\"value\"}"}'

PIXEL_CREATE_API_ENDPOINT = f"https://pixe.la/v1/users/{USER}/graphs/graph1"
cur_date = datetime.now().strftime("%Y%m%d")
yesterday = (datetime.now() - timedelta(1)).strftime("%Y%m%d")
print(cur_date)

create_pixel_param = {
    "date": cur_date,
    "quantity": "1"
}

response = requests.post(PIXEL_CREATE_API_ENDPOINT, json=create_pixel_param, headers=header)
print(response)
print(response.text)