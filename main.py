import requests

# url = "http://google.com"
url = "http://server4.ftpbd.net"
n = 1

def menu():
	print( "+-+-+-+-+ +-+-+-+-+-+-+\n|B|D|I|X| |T|E|S|T|E|R|\n+-+-+-+-+ +-+-+-+-+-+-+" )

def read_urls():

	with open("data/bdix_ip.csv","r") as file:
		lines = [x.split(",")[0] for x in file.readlines()]
	# print(lines)
	return lines

def call_url(url):
	try:
		response = requests.get(url, timeout=n)
		print(response.status_code)
		print(response.elapsed.total_seconds())
	except:
		print("Error!")

def run():
	menu()
	urls = read_urls()

	for i in urls:
		call_url(i)

run()