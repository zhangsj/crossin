#coding:gbk
with open(r'E:\OPS\技术\pylearn\crossin\openfile.py') as fint:
#    outdata=readlines(fint)
    for l in fint.readlines():
        print l
        with open(r'E:\OPS\技术\pylearn\crossin\openfile.txt','a') as fout:
           fout.write(l)

i = raw_input('input the messages:')
with open(r'E:\OPS\技术\pylearn\crossin\openfile.txt','a') as fout:
    fout.write(i)
