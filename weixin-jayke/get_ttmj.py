#coding:utf-8
import requests,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup

# dynm=raw_input('输入名字：')

def get_mj(mjmz):
    auth_url = 'http://www.ttmeiju.com/index.php/user/login.html'
    data = {
        'password': 'xxxxx',
        'username': 'xxxxxx'
    }
    headers = {
        "Host": "www.ttmeiju.com",
        "Referer": "http://www.ttmeiju.com"
    }
    post_data = urllib.urlencode(data)
    cookieJar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
    url = 'http://www.ttmeiju.com/index.php/search/index.html?keyword=%s&range=1' % mjmz
    try:
        op = opener.open(url)
        r=op.read()
        info_list = BeautifulSoup(r, "lxml").find_all('tr', class_=['Scontent', 'Scontent1'])
        if len(info_list)==0:#没搜索到返回没找到
            mjinfo="没找到。。。。。。"
        else:
            mjinfo = ''
            for i in info_list[:3]:#由于字数限制只取前3个
                info=i.find_all('td')
                name1=info[1].find('a').string
                link=''
                for ii in info[2].find_all('a'):
                    link+=(ii['title']+':'+ii['href'])
                size = info[3].string
                format = info[4].string
                mjinfo+=str(name1)+'\t'+str(link)+'\t'+str(size)+'\t'+str(format)+'\n'
        return mjinfo+"form---http://www.ttmeiju.com"
    except:
        mjinfo="没找到。。。。。。"
        return mjinfo
