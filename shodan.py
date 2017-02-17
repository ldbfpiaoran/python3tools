from urllib.request import urlopen
import json 



key = '?key=E48kKXIaCpuKq4nsTJCglvd9o4y8oBni'
#hosturl = 'https://api.shodan.io/shodan/host/'
#req = urlopen(hosturl+'119.97.180.156'+key)


def url_ip(ip):
    hosturl = 'https://api.shodan.io/shodan/host/'
    key = '?key=E48kKXIaCpuKq4nsTJCglvd9o4y8oBni'
    try:
        req = urlopen(hosturl+ip+key)
    except:
        print('错误')
    print(req)
    response = json.loads(req.read().decode('utf-8')) 
    print(response['ports'])
    print(response['city'])
    #print(response['domains'])
        


url_ip('222.33.63.163')
