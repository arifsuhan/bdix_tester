from bs4 import BeautifulSoup
import requests
import re
from lib.FileManager import *

class Crawl:

	def __init__(self,filePath):
		self.filePath = filePath

	def get_soup(self,URL):
		r = requests.get(URL)
		return BeautifulSoup(r.content, 'html.parser')

	def parse(self, soup, base_URL):
		token = "/DHAKA-FLIX-7/"
		# print(base_URL,token)
		base_URL = base_URL.replace(token,"")
		temp = soup.find_all('a',{'href': re.compile(r"^"+ token +"*")})
		return [ {'title': x.text , 'link': base_URL + x['href']} for x in temp]

	def create_playlist(self,filename, data):

		with open(filename,"w") as file:
			file.write("#EXTM3U\n")

			for temp in data:
				file.write("#EXTINF:3244," + temp['title'] + "\n")
				file.write(temp['link'] + "\n")
	
	def run(self):
		urls = FileManager().read2(self.filePath)
		
		for url in urls:
			
			temp_url = "".join(url)
			print(temp_url)
			soup = self.get_soup(temp_url)
			self.parse_object = self.parse(soup, temp_url)

	def save(self,filePath):
		filemanager = FileManager()
		filemanager.write(filePath,self.parse_object)
		site_object = [[temp["link"]] for temp in self.parse_object]
		filemanager.write(self.filePath,site_object)
