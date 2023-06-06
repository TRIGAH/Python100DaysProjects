import requests
from datetime import datetime
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "maps"
TOKEN = "tirootm3445456kk65"
user_parameters = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}

# create_user_response = requests.post(PIXELA_ENDPOINT,json=user_parameters)
# print(create_user_response.text)

graph_params = {
    "id":"graph1",
    "name":"Coding Graph",
    "unit":"M",
    "type":"float",
    "color":"kuro",
}

graph_headers = {
    "X-USER-TOKEN":TOKEN
}

# create_graph_response = requests.post(f"{PIXELA_ENDPOINT}/{USERNAME}/graphs",json=graph_params,headers=graph_headers)
# print(create_graph_response.text)
today = datetime.now()

pixel_params = {
    "quantity":"25.67"
}

# create_pixel_response = requests.post(f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1",json=pixel_params,headers=graph_headers)
# print(create_pixel_response.text)

update_pixel_response = requests.put(f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/20230606",json=pixel_params,headers=graph_headers)
print(update_pixel_response.text)