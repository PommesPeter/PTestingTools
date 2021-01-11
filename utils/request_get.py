import requests
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
    "User-Agent": ua.random,
}

url = "https://support.sas.com/techsup/technote/ts723_Designs.txt"

result = requests.get(url, headers=headers).text

print(result)