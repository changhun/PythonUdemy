import requests

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

response = requests.post(POST_API_ENDPOINT, json=params, headers=header)
print(response.text)