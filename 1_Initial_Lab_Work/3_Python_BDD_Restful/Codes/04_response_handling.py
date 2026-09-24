import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:

    response = requests.get(url)

    print("========== RESPONSE OBJECT ==========")
    print(response)

    print("\n========== STATUS CODE ==========")
    print(response.status_code)

    print("\n========== HEADERS ==========")
    print(response.headers.get("Content-Type"))

    print("\n========== TEXT RESPONSE ==========")
    print(response.text[:100])

    print("\n========== JSON RESPONSE ==========")
    print(response.json())

    print("\n========== CONTENT ==========")
    print(len(response.content), "bytes")

    response.raise_for_status()

    print("\nRequest completed successfully")

except requests.RequestException as error:

    print("Request failed:", error)

finally:

    print("\nResponse handling completed")