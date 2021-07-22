import requests
from tqdm import tqdm 
import os

def menu():
	print( "+-+-+-+-+ +-+-+-+-+-+-+\n|B|D|I|X| |T|E|S|T|E|R|\n+-+-+-+-+ +-+-+-+-+-+-+" )

def read_urls():

	with open("data/bdix_ip.csv","r") as file:
		lines = [x.split(",")[0] for x in file.readlines()]
	# print(lines)
	return lines

def call_url2(url, n = 1):
	try:
		response = requests.get(url, timeout=n)
		# print(response.status_code)
		# print(str(response.elapsed.total_seconds()) + " -> " + url)
		return url
	except:
		# print("Error!")
		print("")

def call_url(url):
	# print(url)
	cmd = "ping -c1 " + url 
	flag = os.system( cmd + ">> /dev/null")

	if flag == 0:
		try:
			res = os.popen(cmd).readlines()[-1]
			t1 = res.split("=")
			# print(t1[0].split("/"))
			# print(t1[1].split("/"))
			avg = float(t1[1].split("/")[1])
			# print(url + "->" +avg)
			return avg
		except:
			return -1
	elif flag == 512:
		# print("Down")
		return -1
	else:
		# print("Error")
		return -1

def run():
	# menu()
	urls = [ x.replace("http://","") for x in read_urls()]
	# urls = [ x.replace("https://","") for x in url()]
	alive_urls = []

	# print(urls)
	# url = "google.com"
	# call_url(url)
	# url = "fs.ebox.live"
	# call_url(url)
	# url = "www.banglanatokhd.com"
	# print(call_url(url))

	# for url in urls:
		# temp = call_url(url)
	

	for url in tqdm(urls, leave=False):
		# print("scanning...")
		# print(i)
		temp = call_url(url)
		if temp!= -1:
			alive_urls.append([url,temp])
			# print(temp)

	res = sorted(alive_urls, key= lambda x: x[1])
	# print(res)

	for i in res:
		print(i)
	

run()

# t1 = [['www.zerodollarmovies.com', '295.987'], ['www.tetrasoftbd.com', '9.621'], ['www.brothersitbd.com', '296.594'], ['www.bijoy.net', '8.996'], ['www.ihub.live', '57.469'], ['www.genvideos.org', '58.693'], ['tube.dfnbd.net', '9.733'], ['www.vdobite.com', '298.905'], ['www.vdomela.com', '9.012'], ['www.broadbandathome.com', '290.043'], ['www.ftpbd.net', '8.973'], ['www.ftpbd.net', '8.543'], ['www.dnetbd.com', '62.455'], ['www.mojaloss.net', '58.013'], ['www.genvideos.org', '59.038'], ['game.zxonlinebd.com', '75.693'], ['www.bigfiveglories.com', '298.119'], ['banglamovieo.blogspot.com', '58.482'], ['www.fullbanglamovie.com', '393.397'], ['www.dailyvision.tv', '398.691'], ['www.jagobd.com', '210.273'], ['www.filehippo.com', '58.293'], ['www.bijoy.net', '9.541'], ['game.zxonlinebd.com', '56.168'], ['www.jagobd.com', '297.833'], ['178.216.250.167', '308.468'], ['www.freetorrentbd.com', '224.145'], ['www.torrentbd.com', '192.743'], ['www.naturalbd.com', '8.563'], ['torrent.dfnbd.net', '10.095'], ['www.antbd.com', '57.759'], ['www.crazyhd.com', '91.495'], ['www.torrentbd.com', '188.311'], ['www.paitara.com', '57.704'], ['server.paitara.com', '63.756'], ['bdixtorrenthome.blogspot.com', '59.291'], ['tube.dfnbd.net', '9.562'], ['www.naturalbd.com', '9.065'], ['www.filehippo.com', '58.766'], ['www.doridro.com', '371.142'], ['www.ihub.live', '57.646'], ['www.pipexbd.com', '9.588'], ['www.jagobd.com', '291.373']]
# t2 = [ [x[0], float(x[1])] for x in t1]
# res = sorted(t2, key= lambda x: x[1])
# print(res)

# for i in res:
# 	print(i)


