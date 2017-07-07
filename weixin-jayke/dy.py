#coding:utf-8
import requests
url='http://www.cswanda.com/movie/play.html'
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A456 Safari/602.1',}
r=requests.get(url,headers=headers)
#with open('dy.txt','w') as f:
#    f.write(r.text.encode('utf-8'))
print r.text       
