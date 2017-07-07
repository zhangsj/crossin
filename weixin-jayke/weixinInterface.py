# -*- coding: utf-8 -*-
import hashlib
import web,sys,re
import lxml
import time
import os
import requests
import simplejson as json
import tianqi
import pic
import getcity
import sys
import dz
import tuling
import get_nhdz
import get_ttmj
from lxml import etree

#city=[u"北京",u"上海"]

class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="xxxxxxxx" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr

        
    def POST(self):        
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        userid = fromUser[0:10]
        toUser=xml.find("ToUserName").text
        if msgType=='text':
            content=xml.find("Content").text#获得用户所输入的内容
            # mm=[u"妹",u"嘿"]
            # pl=[u"笑",u"搞",u"哈",u"呵",u"难"]
            #for m in mm:
	        #    if m in content[:]:
                #	url="http://jandan.net/ooxx/"
                #	mztp=pic.get_one_pic(pic.get_lists(url)) 
                #	return self.render.reply_text(fromUser,toUser,int(time.time()),"http://"+mztp)
            	#	sys.exit()
	        #for p in pl:
	        #    if p in content[:]:
	        #        url="http://jandan.net/pic/"
	        #        gxtp=pic.get_one_pic(pic.get_lists(url)) 
	        #        return self.render.reply_text(fromUser,toUser,int(time.time()),"http://"+gxtp)
	        #    	sys.exit()
	    if re.split(':|：',content.encode("utf-8"))[0]=="美剧":
                mjmz = re.split(':|：', content.encode("utf-8"))[1]
                cont=get_ttmj.get_mj(mjmz)
                return self.render.reply_text(fromUser,toUser,int(time.time()),cont)
            elif content.encode("utf-8")=="功能":
                return self.render.reply_text(fromUser,toUser,int(time.time()),"输入"+"\n"+"妹子图：发送美女图片(太high部分会被微信屏蔽..)"+'\n'+"搞笑图：发送动态搞笑图片"+'\n'+"县市名：查询天气"+"\n"+"段 子：内涵段子"+'\n'+'美剧：美剧名  返回下载地址'+'\n'+"其 它：接入机器人自动回复")
            elif content.encode("utf-8") in getcity.city.keys():
                url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s' % content
                jrtq,gm,mrtq=tianqi.showinfo(url)
                return self.render.reply_text(fromUser,toUser,int(time.time()),jrtq+"\n"+gm+"\n"+"=="*10+"\n"+mrtq)
            elif content.encode("utf-8")=="妹子图":#判断输入的关键字
                url="http://jandan.net/ooxx/"
                mztp=pic.get_one_pic(pic.get_lists(url))
                return self.render.reply_text(fromUser,toUser,int(time.time()),"http://"+mztp)
            #elif len([l for l in content[:] if l in pl])!=0:
            elif content.encode("utf-8")=="搞笑图":
                url="http://jandan.net/pic/"
                gxtp=pic.get_one_pic(pic.get_lists(url))
                return self.render.reply_text(fromUser,toUser,int(time.time()),"http://"+gxtp)
            elif content.encode("utf-8")=="段子":
                dzxx=get_nhdz.nhdz()
                return self.render.reply_text(fromUser,toUser,int(time.time()),dzxx)
            else:
                new_content=tuling.tl(content,userid)
                return self.render.reply_text(fromUser,toUser,int(time.time()),new_content)

        elif msgType=='voice':
            content=xml.find("Recognition").text#获得用户所输入的内容
            try:
                new_content=tuling.tl(content,userid)
                return self.render.reply_text(fromUser,toUser,int(time.time()),new_content)
            except:
                return self.render.reply_text(fromUser,toUser,int(time.time()),'我有点笨，这句我不懂-_-...')
        else:
            return self.render.reply_text(fromUser,toUser,int(time.time()),'图片。。。我看看就好！')
