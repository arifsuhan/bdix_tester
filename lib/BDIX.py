from lib.Client import *
from lib.FileManager import *

class BDIX:

    def __init__(self) -> None:
        pass

    def menu(self,data):
        print( "+-+-+-+-+ +-+-+-+-+-+-+\n|B|D|I|X| |T|E|S|T|E|R|\n+-+-+-+-+ +-+-+-+-+-+-+" )
        print("Site,Accessible")
        
        result = []

        for temp in data:
            if temp['signal'] == "Yes":
                # print(temp["url"])
                result.append({"url": temp["url"]})
        
        if result!=[]:
            FileManager().write("report/result_ip_list.csv",result)

    def config_builder(self): 
        self.timeout = 5
        self.filename = "data/bdix_ip2.csv"

        self.config = {
            "timeout" : self.timeout,
            "filePath" : self.filename
        }

    def client_result(self,data):
        client = Client(self.config["timeout"])
        return client.run(data)

    def run(self):
        self.config_builder()
        urls = FileManager().read(self.config["filePath"])
        data = self.client_result(urls)
        self.menu(data)
