import requests

BASE_URL = "http://sentiment-app-alb-994361147.us-east-1.elb.amazonaws.com"

response = requests.post(
    f"{BASE_URL}/predict",
    json={"text": "This lab maybe took a while but aws was tough"}
)

print("Status code:", response.status_code)
print("Response:", response.json())

assert response.status_code == 200
assert "prediction" in response.json()
