import csv
import json

class FileManager:

    def __init__(self):
        pass

    def read(self,path):
        with open(path,"r") as file:
            lines = [x.split(",")[0] for x in file.readlines()]
        return lines

    def read2(self,filename):

        with open( filename, "r", encoding='utf-8' ) as file_object:

            if ".json" in filename:
                data = json.load(file_object)

            elif ".csv" in filename:     
                csv_reader = csv.reader(file_object)
                data = list(csv_reader)
                
        return data
    
    def write(self,filename,data):

        with open(filename,"a",encoding='utf-8') as file:
        
            if ".json" in filename and type(data[0]) == dict:        
                file.write(json.dumps(data, ensure_ascii=False, indent=4))
                
            elif ".csv" in filename:
                
                key_list = []
                data_list = data

                if type(data[0]) == dict:
                    key_list,data_list = self.dict_to_list(data)
                    header = ",".join([ key for key in key_list]) + "\n"
                    file.write(header)

                for data in data_list:
                    temp = ",".join(data) + "\n"
                    file.write(temp)

    def csv_to_json(self,data):
        pass

    def dict_to_list(self,data_list):
        
        key_list = [ key for key in data_list[0]]
        result = []
        
        for data in data_list:
            temp = [ data[key] for key in key_list]
            result.append(temp)

        return key_list, result