import requests

# url = "https://coronavirus-19-api.herokuapp.com/countries/Bangladesh"
url = ""

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)