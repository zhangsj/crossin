#coding:gbk
from random import shuffle
num=range(1,14)
se=['黑桃','红心','梅花','方片']
wang=['大王','小王']
pai=[]
for i in se:
    for m in num:
        k = i+str(m)
        pai.append(k)
for w in wang:
    pai.append(w)
shuffle(pai)
a=','.join(pai[:17])
b=','.join(pai[17:34])
c=','.join(pai[34:51])
s=','.join(pai[51:])
print 'a的牌: '+a
print 'b的牌: '+b
print 'c的牌: '+c
print '底牌: '+c
