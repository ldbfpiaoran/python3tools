import urllib.request



response = urllib.request.urlopen('http://www.data5u.com')
response = response.read().decode('utf-8')

print(response)
