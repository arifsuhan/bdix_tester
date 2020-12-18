import requests
from tqdm import tqdm 

def menu():
	print( "+-+-+-+-+ +-+-+-+-+-+-+\n|B|D|I|X| |T|E|S|T|E|R|\n+-+-+-+-+ +-+-+-+-+-+-+" )

def read_urls():

	with open("data/bdix_ip.csv","r") as file:
		lines = [x.split(",")[0] for x in file.readlines()]
	# print(lines)
	return lines

def call_url(url, n = 1):
	try:
		response = requests.get(url, timeout=n)
		# print(response.status_code)
		# print(str(response.elapsed.total_seconds()) + " -> " + url)
		return url
	except:
		# print("Error!")
		print("")

def run():
	menu()
	urls = read_urls()
	alive_urls = []

	for i in tqdm(urls, leave=False):
		# print("scanning...")
		temp = call_url(i)
		if temp:
			alive_urls.append(temp)
			# print(temp)
	print(alive_urls)

run()