import requests

result=requests.get("https://open.er-api.com/v6/latest/USD")
data=result.json()
print(data)
