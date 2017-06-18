#coding:utf-8
import urllib2,json
import city
def ctq(name):
    try:
        bianma=city.getcode(name)
        url='http://www.weather.com.cn/data/cityinfo/%s.html' % bianma
        result=urllib2.urlopen(url)
        html=result.read()
        html=json.loads(html)
        info=html['weatherinfo']
        print name
        print info['weather']
        print info['temp1']+'~'+info['temp2']
    except:
        print '输入正确的城市！'
if __name__ == "__main__":
    name = raw_input('你想查询哪个城市的天气：')
    ctq(name)