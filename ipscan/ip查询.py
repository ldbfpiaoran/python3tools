#ip查询位置查询
import urllib.request
import json
import time
import datetime
print('''
 _____   _       ___   _____   _____        ___   __   _  
|  _  \ | |     /   | /  _  \ |  _  \      /   | |  \ | | 
| |_| | | |    / /| | | | | | | |_| |     / /| | |   \| | 
|  ___/ | |   / / | | | | | | |  _  /    / / | | | |\   | 
| |     | |  / /  | | | |_| | | | \ \   / /  | | | | \  | 
|_|     |_| /_/   |_| \_____/ |_|  \_\ /_/   |_| |_|  \_|
''')

def get_ip(ip):
    
#ip = '222.33.63.163'
    ip_addrs = 'http://api.map.baidu.com/highacciploc/v1?qcip='+ip+'&qterm=pc&ak=SNjRPTGuQEyMK41FguGgxPFGGNmDkyQG&coord=bd09ll&extensions=3'
#print(ip_addrs)

    req = urllib.request.Request(ip_addrs)
    req.add_header = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/5.7.16173.12 Safari/537.36')
    html = urllib.request.urlopen(req)
    html = html.read().decode('utf-8')
    data_dict = json.loads(html)
    try:
        content = data_dict['content']
        city = content['formatted_address']
        print('地理位置为：'+city)
        print(datetime.date.today())
    except:
        print('未找到该ip')

def loop():
    ex = 1
    while ex == 1:
        ip = input('请输入ip地址(退出请输入q)： ')
        ip = str(ip)
        if ip == 'q':
            ex = 2
            print('正在退出请稍等3秒')
        else:
            get_ip(ip)
        time.sleep(3)



if __name__ == '__main__':
    loop()
