#coding:utf-8
#Hello Mr.张，welcome you to 南京。
import re

#取出单词，并排序
with open('from.txt','r') as f:
    rdf=f.readlines()
    m=re.findall(r'\b[a-zA-Z]+[a-zA-Z]\b',rdf[0])
    m.sort()
#写入新的文件
with open('to.txt','w') as w:
    for l in m:
        w.write(l+'\n')