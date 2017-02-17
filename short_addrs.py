from urllib.request import urlopen
from bs4 import BeautifulSoup
print('''
 _____   _       ___   _____   _____        ___   __   _  
|  _  \ | |     /   | /  _  \ |  _  \      /   | |  \ | | 
| |_| | | |    / /| | | | | | | |_| |     / /| | |   \| | 
|  ___/ | |   / / | | | | | | |  _  /    / / | | | |\   | 
| |     | |  / /  | | | |_| | | | \ \   / /  | | | | \  | 
|_|     |_| /_/   |_| \_____/ |_|  \_\ /_/   |_| |_|  \_|
''')


addrs = str(input('输入要缩写的短域名'))

inurl = 'http://suo.im/api.php?format=jsonp&url='+addrs

req = urlopen(inurl)

response = BeautifulSoup(req.read(),"html.parser")



print(response)
                         

