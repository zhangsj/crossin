#coding:gbk
import time,linecache
while True:
    print "1.查账;2.记账"
    c = raw_input('请选择服务:')
    if c.isdigit():
        try:
            c=int(c)
            if c==1:
                print '查账模式\n1.查询最近十笔交易记录\n2.查询与某公司交易往来\n3.查询最近资产负债状况'
                cc=input('请选择查询条目:')
                if cc==1:
                    print '\n'.join(linecache.getlines('流水账单.txt')[-8:])
            elif c==2:
                print "记账模式"
                ob = raw_input('交易对象:')
                sr = str(input('收入/万：'))
                zc = str(input('支出/万：'))
                ys = str(input('应收账款/万：'))
                yc = str(input('应出帐款/万：'))
                line='\n'+ob+'\t'+sr+'\t'+zc+'\t'+ys+'\t'+yc+'\t'+time.strftime('%Y-%m-%d',time.localtime())
                print line
                with open(r'流水账单.txt','a') as jz:
                    jz.write(line)

        except:
            print '输入错误'
            continue
    else:
        continue
