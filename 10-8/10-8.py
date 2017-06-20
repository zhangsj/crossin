#coding:utf-8
import json,urllib2,requests
from gzip import GzipFile
from StringIO import StringIO
import zlib
# city=raw_input('请输入城市：')
url='http://wthrcdn.etouch.cn/weather_mini?city=%s' % '郏县'
#如果gzip解压
def loadData(url):
    request = urllib2.Request(url)
    request.add_header('Accept-encoding', 'gzip,deflate')
    response = urllib2.urlopen(request)
    content = response.read()
    encoding = response.info().get('Content-Encoding')
    if encoding == 'gzip':
        content = ugzip(content)
        # print content
    elif encoding == 'deflate':
        content = udeflate(content)
    return content

def ugzip(data):
    buf = StringIO(data)
    f = GzipFile(fileobj=buf)
    return f.read()

def udeflate(data):
    try:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)
#读取日期天气风温度信息
def rinfo(self):
    riqi=self.get('date')
    wendu1=self.get('low')
    wendu2=self.get('high')
    tq=self.get('type')
    fl=self.get('fengli')
    fx=self.get('fengxiang')
    return riqi,tq,fl,fx,wendu1,wendu2
#展示天气信息
def showinfo(url):
    info=loadData(url)
    info=json.loads(loadData(url)).get('data')
    ganmo=info.get('ganmao')
    today=info.get('forecast')[0]
    tom=info.get('forecast')[1]
    aftom1=info.get('forecast')[2]
    aftom2=info.get('forecast')[3]
    aftom3=info.get('forecast')[4]
    print '今日天气：\n日期:%s\n天气：%s\n风:%s\t%s\n温度：%s,%s'% rinfo(today)
    print '感冒指数:%s' % ganmo
    print "="*20
    print '明天天气：\n日期:%s\n天气：%s\n风:%s\t%s\n温度：%s,%s'% rinfo(tom)

if __name__=='__main__':
    try:
        city = raw_input('请输入城市：')
        url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s' % city
        if json.loads(requests.get(url).content).get('status')==1000:#直接使用request模块，判断城市是否存在，城市存在则返回1000
            print city
            showinfo(url)
        else:
            print "查询失败"
    except Exception,e:
        print e

