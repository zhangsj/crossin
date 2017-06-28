#coding:utf-8
import requests,re

url = "http://jandan.net/pic"
url = "http://jandan.net/ooxx"
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

def find_images(url):
    html=getpic(url)
    img_src0=re.findall(r'((<img\ssrc|\sorg_src)="//.{,80}.(gif|jpg|png))', html)
    print img_src0
    #从包含图片源地址的这一段字符串中提取图片的源地址
    img_src1=[img_src[12:] for img_src in img_src0]
    # print img_src1
    return img_src1


def download_mm(folder='mmImages', pages=10):
    """
   下载十个页面的图片,并将其保存进folder目录
    """

    # 创建保存图片的文件夹
    # os.mkdir('folder')
    # os.chdir('folder')
    # 下载图片页面初始地址
    url = 'http://jandan.net/ooxx/'
    # 图片页面地址全名为http://jandan.net/ooxx/page-2364#comments,可看出图片地址为'url'+'页面数'+ '#comments',先定义一个函数get_page(url)来获取page_num
    page_num = int(get_pagenum(url))

    # 有了图片所在页面的全名地址就可以爬取图片的源地址了,这里我们仅下载十个页面的图片
    for i in range(pages):
        page_num -= i
        # 获得十个网页的图片地址,进入页面时我们处于最新页面,因此最终得到的是此页以及前九页的地址
        page_url = url + "page-"+ str(page_num) + '#comments'
        # 获得多个图片网址后还需获得每一个图片的源地址才能下载到每一张图片,此处定义一个函数find_images来获取每张图片源地址
        img_addrs = find_images(page_url)
        # 从每张图片源地址下载图片到folder文件夹
        # save_imgs(folder, img_addrs)
        # print img_addrs
download_mm()