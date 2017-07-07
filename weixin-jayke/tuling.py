#coding:utf-8
import requests,json
global s
s = requests.session()
#content=raw_input("说吧：")
def tl(content,userid):
    url='http://www.tuling123.com/openapi/api'
    text={"key":"xxxxxxxxxxxx","info":content,"userid":userid}
    p_text=json.dumps(text)
    res=s.post(url,data=p_text)
    j=eval(res.text)
 #   print j
  #  print j['text']
    code=j['code']
    if code==100000:
        newcontent=j['text']
    if code==200000:
        newcontent=j['text']+j['url']
   # print newcontent
    return newcontent
#tl(content)            
