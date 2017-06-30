#coding:utf-8
import requests,re,random
from bs4 import BeautifulSoup
url="http://www.54ssz.com/mldz/"
def get_home(url):#读取url内容
    res=requests.get(url)
    return res
def get_page(url):#获取所有子页面，并随机返回一个子页面
    u_txt=get_home(url).text
    # print u_txt.text
    page=[]
    page+=re.findall(r"http://www.54ssz.com/mldz/.{4,20}.html",u_txt)
    page=list(set(page))
    onepage=random.sample(page,1)
    # print page,onepage
    print onepage
    return onepage[0]

def re_xh(url):#在子页面中截取文字的部分
    txt=get_home(url)
    txt.coding='utf-8'
    xh_text=BeautifulSoup(txt.content,'lxml')
    # print xh_text
    try:# one_xh=random.sample(xh_text.find_all(text=re.compile('^(\r\n)?[1|2|3|4|5][.|、]')),1)[0]#匹配数字开头带.的字段1前面有1回车和换行，在列表中随机返回一个，
        one_xh = random.sample(xh_text.find_all(text=re.compile('^(\r\n)?[1|2|3]\.')), 1)[0]
        print one_xh[2:]
    except:
        one_xh = random.sample(xh_text.find_all(text=re.compile(u'\d、')), 1)[0]
    # return one_xh[1:]#去掉段子前面的数字和.
        print one_xh[5:]


re_xh(get_page(url))
