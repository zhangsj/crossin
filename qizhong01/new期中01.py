#coding:utf-8
import pandas as pd
import numpy as np
f=open('report.txt')
lines=f.readlines()
f.close()
new4=[]
n_data=[]
spj=[]
m=1
info="名次\t姓名\t语文\t数学\t英语\t物理\t化学\t生物\t政治\t历史\t地理\t总分\t平均分\n"
for li in lines:
    l = []
    li=li.split()
    l.append(li[0])
    l.extend([int(x) for x in li[1:]])
    l.append(sum(l[1:]))
    l.append('%.1f' % (float(l[-1])/len(l[1:-1])))
    n_data.append(l)
for x in range(1,11):
    pj=0
    for cj in n_data:
        pj+=int(cj[x])
    spj.append(pj/30)
spj.append('%.1f' % (float(spj[-1])/len(spj[:-1])))
spj.insert(0,0)
spj.insert(1,'平均')
spj=[str(x) for x in spj]
new1=sorted(n_data,key=lambda pj:pj[-1],reverse=True)
for new2 in new1:
    new3=['不及格' if x < 60 else x for x in new2[1:]]
    new3.insert(0,new2[0])
    new3=[str(x) for x in new3]
    new4.append(new3)
outfile=('newreport.txt')
o=open(outfile,'a')
o.write(info)
xpj='\t'.join(spj)+'\n'
o.write(xpj)
o.close()
# print new4
for new in new4:
    new.insert(0,str(m))
    m+=1
    with open(outfile,'a') as wf:
        print new
        enf='\t'.join(new)+'\n'
        wf.write(enf)


