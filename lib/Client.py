import requests
from requests.exceptions import ConnectTimeout
from datetime import datetime
from tqdm import tqdm

class Client:

    def __init__(self,timeout) -> None:
        self.timeout = timeout

    def call(self,url):
        
        result = {}
        now = datetime.now()
        formatted_now = now.strftime('%y-%m-%d %H:%M:%S') + f':{now.microsecond // 1000:03d}'
        status = ""
        signal = ""

        try:
            response = requests.get(url, timeout=self.timeout)
            status = response.status_code
            elapsed_time = response.elapsed.total_seconds()
            signal = 1

        except ConnectTimeout:
            status = "ConnectTimeout"
            signal = 0
            
        
        except requests.ConnectionError:
            status = "ConnectionError"
            signal = 0

        except Exception as e:
            status = e
            signal = -1

        result = {
            "url" : url,
            "status" : status,
            "signal" : signal,
            "updateTime" : str(formatted_now)
        }
        
        return result

    def run(self,urls):
        
        result = []
        # print(urls)

        for url in tqdm(urls):
            response = {}
            response = self.call(url)
            response["signal"] = "Yes" if response['signal'] == 1 else "No"
            result.append(response)
        
        return result

        
