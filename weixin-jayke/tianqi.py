#coding:utf-8
import requests,json
#chengshi='上海'
#url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s' % chengshi

def rinfo(self):
    riqi=self.get('date')
    wendu1=self.get('low')
    wendu2=self.get('high')
    tq=self.get('type')
    fl=self.get('fengli')[10:-3]
    fx=self.get('fengxiang')
    return riqi,tq,fl,fx,wendu1,wendu2
#展示天气信息
def showinfo(url):
    r=requests.get(url).content
    info=json.loads(r).get('data')
    # print info
    ganmao=info.get('ganmao')
    today=info.get('forecast')[0]
    tom=info.get('forecast')[1]
    aftom1=info.get('forecast')[2]
    aftom2=info.get('forecast')[3]
    aftom3=info.get('forecast')[4]
    jinritianqi=u'今日天气：\n日期:%s\n天气：%s\n风:%s\t%s\n温度：%s,%s'% rinfo(today)
    mingritianqi=u'明日天气：\n日期:%s\n天气：%s\n风:%s\t%s\n温度：%s,%s'% rinfo(tom)
    # print u'今日天气：\n日期:%s\n天气：%s\n风:%s\t%s\n温度：%s,%s'% rinfo(today)
    # print u'感冒指数:%s' % ganmao
    # print "="*20
    # print u'明天天气：\n日期:%s\n天气：%s\n风:%s\t%s\n温度：%s,%s'% rinfo(tom)
    # print jinritianqi
    return jinritianqi,ganmao,mingritianqi

#if chengshi in city.city.keys():
#    jrtq,gm,mrtq=showinfo(url)
#    print jrtq+'\n'+gm+'\n'+mrtq
