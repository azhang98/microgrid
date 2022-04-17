import requests
url = 'http://192.168.6.9:80/wind-PWM'
myobj = {'voltage': '12.2', 'current' : '2.3', 'battery' : '13.4'}

x = requests.get(url)

print(x.text)
