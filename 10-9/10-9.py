#coding:utf-8
import re
with open('wenben.txt','r') as f:
    w=f.read()
    m=re.findall(r'\b[a-zA-Z]+',w)
    print 'There are %s words in words.txt.' % len(m)