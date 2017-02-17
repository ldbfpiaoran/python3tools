from bs4 import BeautifulSoup
import requests


def get_url(key,pagenum):
    
    url = 'https://www.baidu.com/s?wd='+key+'&pn='+pagenum
    
    head = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17"}
    req = requests.get(url,headers=head).text
    #print(req)
    response = BeautifulSoup(req,"html.parser")
    #print(response)
    resq =response.findAll('div',{'class':'f13'})
    link = []
    urllink = []
    for i in resq:
        try:
            if i.find('a',{'target':'_blank'})['href'].startswith("http://"):
                link.append(i.find('a',{'target':'_blank'})['href'])
        except:
            print('>>>有一条出错啦')
    for i in link:
        page = requests.get(i,headers=head,allow_redirects=False)
        if page.status_code == 200:
            u = re.search(r'URL=\'(.*?)\'', tmpPage.text.encode('utf-8'), re.S)
            urllink.append(u.group(1))
        elif page.status_code == 302:
            u = page.headers.get('location')
            urllink.append(u)
        else:
            print('解析出错啦')
    for i in urllink:
        print(i)
    
    
key = str(input('请输入要查询的内容'))
pagenum = int(input('请输入要查询的页数'))
pagenum -= 1
pagenum = pagenum*10

for i in range(0,pagenum+1,10):
    i = str(i)
    get_url(key=key,pagenum=i)
    



