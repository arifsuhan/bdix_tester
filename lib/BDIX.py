from lib.Client import *
from lib.FileManager import *

class BDIX:

    def __init__(self) -> None:
        pass

    def menu(self,data):
        print( "+-+-+-+-+ +-+-+-+-+-+-+\n|B|D|I|X| |T|E|S|T|E|R|\n+-+-+-+-+ +-+-+-+-+-+-+" )
        print("Site,Accessible")
        for temp in data:
            print(temp)


    def config_builder(self): 
        self.timeout = 5
        self.filename = "data/bdix_ip.csv"

        self.config = {
            "timeout" : self.timeout,
            "filePath" : self.filename
        }

    def client_result(self,data):
        client = Client(self.config["timeout"])
        return client.run(data)

    def run(self):
        self.config_builder()
        urls = FileManager().read(self.config["filePath"])[:10]
        data = self.client_result(urls)
        self.menu(data)
