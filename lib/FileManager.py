class FileManager:

    def __init__(self) -> None:
        pass

    def read(self,path):
        with open(path,"r") as file:
            lines = [x.split(",")[0] for x in file.readlines()]
        return lines