import requests

# url = "https://coronavirus-19-api.herokuapp.com/countries/Bangladesh"
url = "http://google.com"
n = 1

payload={}
headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)
response = requests.get(url, timeout=n)

# print(response.text)
# print(response.status_code)
print(response.elapsed.total_seconds())




import subprocess
import ipaddress

alive = []
# subnet = ipaddress.ip_network('192.168.1.0/23', strict=False)
url = ["google.com"]

for i in url:
    i = str(i)
    # retval = subprocess.call('ping -c 1 google.com',stdout=subprocess.DEVNULL)
    retval = subprocess.call('ping -c 1 %s' % str(i))
    if retval == 0:
        alive.append(i)
for ip in alive:
    print(ip + " is alive") 