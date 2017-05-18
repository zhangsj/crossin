#coding:gbk
a=input("身高:")
b=input("体重:")
c=b/(a**2)
if c < 18.5:
    print "%f、偏轻" % c
elif c >= 24:
        print "%f、偏重" % c
else:
    print "%f、正常" % c
