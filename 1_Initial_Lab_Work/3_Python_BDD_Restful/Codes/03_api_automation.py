import requests
import json


BASE_URL = "https://jsonplaceholder.typicode.com"


# Read external test data
with open("TestData/api_data.json", "r") as file:
    data = json.load(file)

print("Test Data:", data)


# GET
response = requests.get(
    BASE_URL + "/posts/1"
)

print("GET:", response.status_code)


# POST
response = requests.post(
    BASE_URL + "/posts",
    json=data
)

print("POST:", response.status_code)


# PUT
response = requests.put(
    BASE_URL + "/posts/1",
    json=data
)

print("PUT:", response.status_code)


# PATCH
response = requests.patch(
    BASE_URL + "/posts/1",
    json={
        "title": "Updated Title"
    }
)

print("PATCH:", response.status_code)


# DELETE
response = requests.delete(
    BASE_URL + "/posts/1"
)

print("DELETE:", response.status_code)