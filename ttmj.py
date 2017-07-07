#coding:utf-8
import requests,sys,re
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup


def get_mj(mjmz):
    url = 'http://www.ttmeiju.com/index.php/search/index.html?keyword=%s&range=1' % mjmz
    r = requests.get(url)
    info_list = BeautifulSoup(r.text, "lxml").find_all('tr', class_=['Scontent', 'Scontent1'])
    print info_list
    if len(info_list)==0:
        mjinfo="没找到。。。。。。"
    else:
        mjinfo = ''
        for i in info_list:
            info=i.find_all('td')
            name1=info[1].find('a').string
            link=''
            for ii in info[2].find_all('a'):
                link+=(ii['title']+':'+ii['href'])
            size = info[3].string
            format = info[4].string
            mjinfo+=str(name1)+'\t'+str(link)+'\t'+str(size)+'\t'+str(format)+'\n'
    return mjinfo
dynm=raw_input('输入名字：')
if re.split(':|：',dynm)[0]=="美剧":
    mjmz = re.split(':|：', dynm)[1]
    cont=get_mj(mjmz)
    print cont

