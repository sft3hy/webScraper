import certifi
import requests

url = 'https://www.intellipedia.intelink.gov'
x = requests.get(url, cert='cac.pem').text

print(x)