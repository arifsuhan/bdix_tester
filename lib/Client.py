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

        try:
            response = requests.get(url, timeout=self.timeout)
            status_code = response.status_code
            elapsed_time = response.elapsed.total_seconds()
            result = {
                'url' : url,
                'status' : status_code,
                'time' : elapsed_time,
                'signal' : 1
            }

        except ConnectTimeout:
            result = {
                'status' : 'ConnectTimeout',
                'signal' : 0
            }

        except Exception as e:
            result = {
                'status' : e,
                'signal' : -1
            }

        result["updateTime"] = str(formatted_now)
        
        return result

    def run(self,urls):
        
        result = []

        for url in tqdm(urls):
            temp = {}
            response = self.call(url)
            signal = response['signal']
            print(signal)

            if signal:
                temp['time'] = response['time']

            signal = "Yes" if response['signal'] else "No"
            temp['url'] = url
            temp['signal'] = signal
            result.append(temp)
        
        return result

        
