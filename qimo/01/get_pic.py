#coding:utf-8
import requests,re,os,urllib2
from time import ctime
from bs4 import BeautifulSoup
import threading

url = "http://jandan.net/ooxx"
def getpic(url):
    res=requests.get(url,timeout=30)
    return res.text

def get_max_page(req):
    max_page = BeautifulSoup(req,'lxml').select('.current-comment-page')[0].string[1:-1]
    print u'最大页码为%s,请输入1-%s'% (max_page,max_page)
    return max_page

def check_page(page,max_page):
    check=True
    max_page+=1
    while check:
        if not (page.isdigit() and int(page) in range(1,max_page)):
            page=raw_input('输入错误，请输入正确的"数字":')
        else:
            check=False
            return int(page)

def input_page(max_page):
    Test=True
    while Test:
        start_page=raw_input('起始页:')
        start_page=check_page(start_page,max_page)
        end_page=raw_input('结束页:')
        end_page=check_page(end_page,max_page)
        if start_page > end_page:
            print '起始页不能大于结束页,请重新输入抓取范围！！'
        else:
            Test=False
            return start_page,end_page

def find_images(url):
    html=getpic(url)
    img_src0=re.findall(r'(<img\ssrc="//.{,80}.jpg|\sorg_src="//.{,80}.gif)', html)
    #从包含图片源地址的这一段字符串中提取图片的源地址
    img_src1=[img_src[12:] for img_src in img_src0]
    return img_src1

#获取图片名字
def get_imgname(img_url):
    file_name=re.findall(r'.+(/.*)',img_url)[0]
    return file_name[1:]

#保存图片
def save_img(url,file_name):
    f=open(file_name,'wb')
    req=urllib2.urlopen(url)
    buf=req.read()
    f.write(buf)

#下载图片
def download_mm(folder,url):
    # 创建保存图片的文件夹
    if os.path.exists(folder):
        os.chdir(folder)
    else:
        os.mkdir(folder)
        os.chdir(folder)
    # 下载图片页面初始地址
    try:
        req=getpic(url)
        max_page=int(get_max_page(req))
        pages=input_page(max_page)
        print 'Start at '+ctime()
        for i in range(pages[0],pages[1]+1):
            page_url=url + "page-"+ str(i) + '#comments'
            for img_addr in find_images(page_url):
                img_name=str(i)+'-'+get_imgname(img_addr)
                img_addr = 'http://' + img_addr
                save_img(img_addr, img_name)
        print 'End at ' + ctime()
    except Exception,e:
        print e

if __name__ == '__main__':
    folder='mmimages'
    url = 'http://jandan.net/ooxx/'
    t=threading.Thread(target=download_mm,args=(folder,url))# 多线程抓取
    t.setDaemon(True)# 声明守护线程
    t.start()# 开始线程活动
    t.join()# 阻塞主线程，保证所有子线程都能完全运行结束
    print 'Over at '+ctime()
