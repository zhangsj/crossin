#coding:utf-8
import json,urllib2,requests
from gzip import GzipFile
from StringIO import StringIO
import zlib
# city=raw_input('请输入城市：')
url='http://wthrcdn.etouch.cn/weather_mini?city=%s' % '郏县'

def loadData(url):
    request = urllib2.Request(url)
    request.add_header('Accept-encoding', 'gzip,deflate')
    response = urllib2.urlopen(request)
    content = response.read()
    encoding = response.info().get('Content-Encoding')
    if encoding == 'gzip':
        content = gzip(content)
        print content
    elif encoding == 'deflate':
        content = deflate(content)
    return content

def gzip(data):
    buf = StringIO(data)
    f = gzip.GzipFile(fileobj=buf)
    return f.read()

def deflate(data):
    try:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)

loadData(url)