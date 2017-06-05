#coding:utf-8
f=open('report.txt')
lines=f.readlines()
f.close()
new4=[]
m=0
for l in lines:
    s=0
    l=l.split()
    # print l
    new2=[]
    for n in l[1:]:
        # print n
        s+=int(n)
        # print l
    p=s/len(l[1:])
    new_l=['不及格' if int(x) < 60 else x for x in l[1:]]
    new2.insert(0,l[0])
    new3=new2+new_l+[str(s),str(p)]
    new4.append(new3)
new5=sorted(new4,key=lambda pj:pj[-1],reverse=True)
info="名次\t姓名\t语文\t数学\t英语\t物理\t化学\t生物\t政治\t历史\t地理\t总分\t平均分\n"
outfile=('newreport.txt')
o=open(outfile,'w')
o.write(info)
o.close()
for new in new5:
    new.insert(0,str(m))
    m+=1
    with open(outfile,'a') as wf:
        print new
        enf='\t'.join(new)+'\n'
        wf.write(enf)

