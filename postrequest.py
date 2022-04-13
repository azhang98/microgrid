import requests
url = 'http://192.168.6.9:80/wind-data'
myobj = {'voltage': '12.2', 'current' : '2.3', 'battery' : '13.4'}

x = requests.post(url, data = myobj)

print(x.text)