#coding:utf-8

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
                    print '最近十笔交易\n交易对象\t收入\t支出\t应收账款\t应付帐款\t交易时间'
                    linecache.updatecache(u'流水账单.txt')
                    for jyjl in linecache.getlines(u'流水账单.txt')[-10:]:
                        jl=jyjl.split()
                        print '%-10s\t%-2s万\t%-2s万\t%-2s万\t\t%-2s万\t\t%s' % tuple(jl)

                if cc==2:
                    gname=raw_input('请输入公司名:')
                    with open(u'流水账单.txt','r') as cgs:
                        ctime=0
                        jywl=[]
                        for line in cgs.readlines()[1:]:
                            line1=line.split()
                            if gname in line1:
                                ctime+=1
                                jywl.append(line1)
                        if ctime==0:
                            print '没有与%s的交易记录' % gname
                        else:
                            print '与%s共有%s次交易' % (gname,ctime)
                            for wl in jywl:
                                print '交易时间：%s\n收入：%s\n支出：%s\n应收账款：%s\n应出账款：%s\n' % (wl[-1], wl[-5], wl[-4], wl[--3], wl[-2])
                if cc==3:
                    with open (u'资产负债表.txt','r') as cfz:
                        fzjl=cfz.readlines()
                        zxfz=fzjl[-1].split()
                        print '\n最新资产：%s万\n最新负债：%s万\n最新净资产：%s万\n最后更新时间：%s\n\n' % (zxfz[1],zxfz[2],zxfz[3],zxfz[0])
                else:
                    print '请输入对应的数字!'
            elif c==2:
                print "记账模式"
                ob = raw_input('交易对象:')
                sr = str(input('收入/万：'))
                zc = str(input('支出/万：'))
                ys = str(input('应收账款/万：'))
                yc = str(input('应出帐款/万：'))
                line='\n'+ob+'\t'+sr+'\t'+zc+'\t'+ys+'\t'+yc+'\t'+time.strftime('%Y-%m-%d',time.localtime())
                with open(u'流水账单.txt','a') as jz:
                    jz.write(line)
                with open (u'资产负债表.txt','a+') as gxfz:
                    syjl=gxfz.readlines()
                    zxjl=syjl[-1].split()
                    newzc=int(zxjl[1])+int(sr)-int(zc)
                    newfz=int(zxjl[2])+int(yc)-int(ys)
                    newjzc=newzc-newfz
                    newfzb='\n'+time.strftime('%Y-%m-%d',time.localtime())+'\t'+str(newzc)+'\t'+str(newfz)+'\t'+str(newjzc)
                    gxfz.write(newfzb)
            else:
                print '请输入对应的数字!'
        except:
            print '输入错误'
            continue
    else:
        print '请输入对应的数字!'
        continue
