#coding:utf-8
import requests,re,random

#url = "http://jandan.net/pic/"
# url = "http://jandan.net/ooxx/"
def getpic(url):
    res=requests.get(url,timeout=30)
    return res.text

def get_pagenum(url):
    html=getpic(url)
    # print html
    page = re.findall(r'page-[0-9]+\b', html)[3]
    # print page
    page_number = re.findall(r'[0-9]+', page)
    # print page_number[0]
    return page_number[0]

def find_mm_images(url):
    html=getpic(url)
    img_src0=re.findall(r'(<img\ssrc="//.{,80}.jpg|\sorg_src="//.{,80}.gif)', html)
    # img_gif_src0 = re.findall(r'\sorg_src="//.{,80}.gif', html)
    # print img_src0
    #从包含图片源地址的这一段字符串中提取图片的源地址
    img_src1=[img_src[12:] for img_src in img_src0]
    # print img_src1
    return img_src1

def find_gx_images(url):
    html=getpic(url)
    img_src0=re.findall(r'\sorg_src="//.{,80}.gif', html)
    # img_gif_src0 = re.findall(r'\sorg_src="//.{,80}.gif', html)
    # print img_src0
    #从包含图片源地址的这一段字符串中提取图片的源地址
    img_src1=[img_src[12:] for img_src in img_src0]
    # print img_src1
    return img_src1


def get_lists(url,pages=10):
    # url = 'http://jandan.net/ooxx/'
    # 图片页面地址全名为http://jandan.net/ooxx/page-2364#comments,可看出图片地址为'url'+'页面数'+ '#comments',先定义一个函数get_page(url)来获取page_num
    page_num = int(get_pagenum(url))
    pic_list=[]
    # 有了图片所在页面的全名地址就可以爬取图片的源地址了,这里我们仅记录十个页面的图片
    for i in range(pages):
        page_num -= i
        # 获得十个网页的图片地址,进入页面时我们处于最新页面,因此最终得到的是此页以及前九页的地址
        page_url = url + "page-"+ str(page_num) + '#comments'
        # 获得多个图片网址后还需获得每一个图片的源地址,如果是美女的url则返回所有类型图片，否则只返回
        if "ox" in url:
            img_addrs = find_mm_images(page_url)
        else:
            img_addrs = find_gx_images(page_url)
        pic_list+=img_addrs
    # print pic_list
    return pic_list

def get_one_pic(pic_list):
    return random.sample(pic_list,1)[0]

