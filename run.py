from lib.BDIX import *
from lib.Crawl import *

# bdix = BDIX()
# bdix.run()

# URL = "http://172.16.50.7/DHAKA-FLIX-7/"
# URL = "http://172.16.50.7/DHAKA-FLIX-7/3D%20Movies/"

crawl = Crawl("data/crawler_ip.csv")
crawl.run()
crawl.save("report/result.csv")