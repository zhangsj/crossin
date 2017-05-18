#coding:utf-8
import re
f=open(r'E:\OPS\test\pylearn\crossin\code.txt')
lines=f.read()
f.close()
# print lines
def ch(self):
    ss=self.split()
    l=lines.split('\n')
    l2=[]
    for l1 in l:
        l1=l1.lower()
        l2.append(l1)
    re=[]
    for s in ss:
        # print type(s)
        if s.lower() in l2:
            s = '*'
            # print s,l
        re.append(s)
    outcode=' '.join(re)


    print outcode
incode=raw_input('请输入一段话:')
incode = incode
ch(incode)
#编辑器 code.txt 都要使用一致的编码 或者decode转码
        
        
    
