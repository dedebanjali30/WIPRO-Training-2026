import requests

base_url = "https://jsonplaceholder.typicode.com"

# GET request
print("========== GET REQUEST ==========")

response = requests.get(
    base_url + "/posts/1"
)

print("Status Code:", response.status_code)
print("Content Type:", response.headers.get("Content-Type"))
print("Response:", response.json())


# POST request
print("\n========== POST REQUEST ==========")

data = {
    "title": "Python Test",
    "body": "API Automation",
    "userId": 1
}

response = requests.post(
    base_url + "/posts",
    json=data
)

print("Status Code:", response.status_code)
print("Response:", response.json())