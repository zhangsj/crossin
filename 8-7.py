#coding:gbk
score=r'E:\OPS\技术\pylearn\crossin\scores.txt'
output=r'E:\OPS\技术\pylearn\crossin\output.txt'
re=[]
print score
with open(score) as f:
    data=f.readlines()
for m in data:
    s=0
    n=m.split()
    for x in n[1:]:
        s+=int(x)       
    r='%s\t: %d\n' % (n[0],s)
    print type(r)
    print r
    re.append(r)
print re
#with open(output,'w') as out:
#    out.writelines(re)

