#coding:utf-8
import os,time,linecache

lszd=u'流水账单.txt'
zcfzb=u'资产负债表.txt'

def init_bill(lszd,zcfzb):
    if not os.path.exists(zcfzb):
        with open(zcfzb,'w') as f:
            f.write('结算日期\t资产/W\t负债/W\t净资产/W\n')
            # f.write('%s\t%s\t%s\t%s\n' % ('2000-01-01',0,0,0))
    if not os.path.exists(lszd):
        with open(lszd,'w') as f:
            f.write('交易对象\t收入/W\t支出/W\t应收账款/W\t应出帐款/W\t交易日期\n')
            # f.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (0,0,0,0,0,'2000-01-01'))
def read_file(self):
    with open(self,'r') as f:
        return f.readlines()
def cz_jl(lszd):
    if len(read_file(lszd)) ==1:
        print '没有任何记录'
    else:
        print '最近十笔交易\n交易对象\t收入\t支出\t应收账款\t应付帐款\t交易时间'
        linecache.updatecache(lszd)
        for jyjl in linecache.getlines(lszd)[-10:]:
            jl = jyjl.split()
            print '%-10s\t%-2s万\t%-2s万\t%-2s万\t\t%-2s万\t\t%s' % tuple(jl)
def cz_gs(lszd):
    gname = raw_input('请输入公司名:')
    ctime = 0
    jywl = []
    for line in read_file(lszd)[1:]:
        line1 = line.split()
        if gname in line1:
            ctime += 1
            jywl.append(line1)
    if ctime == 0:
        print '没有与%s的交易记录' % gname
    else:
        print '与%s共有%s次交易' % (gname, ctime)
        for wl in jywl:
            print '交易时间：%s\n收入：%s\n支出：%s\n应收账款：%s\n应出账款：%s\n' % (wl[-1], wl[-5], wl[-4], wl[--3], wl[-2])
def cz_fz(zcfzb):
    if len(read_file(zcfzb))==1:
        print '还么有任何记录'
    else:
        fzjl = read_file(zcfzb)
        zxfz = fzjl[-1].split()
        print '\n最新资产：%s万\n最新负债：%s万\n最新净资产：%s万\n最后更新时间：%s\n\n' % (zxfz[1], zxfz[2], zxfz[3], zxfz[0])

def jz(lszd,zcfzb):
    print "记账模式"
    ob = raw_input('交易对象:')
    sr = str(input('收入/万：'))
    zc = str(input('支出/万：'))
    ys = str(input('应收账款/万：'))
    yc = str(input('应出帐款/万：'))
    line = '\n' + ob + '\t' + sr + '\t' + zc + '\t' + ys + '\t' + yc + '\t' + time.strftime('%Y-%m-%d',time.localtime())
    with open(lszd, 'a') as jz:
        jz.write(line)
    with open(zcfzb, 'a+') as gxfz:
        if len(gxfz.readlines())==1:
            newzc=int(sr)+int(ys)
            newfz=int(zc)+int(yc)
            newjzc=newzc-newfz
            newfzb='\n' + time.strftime('%Y-%m-%d', time.localtime()) + '\t' + str(newzc) + '\t' + str(newfz) + '\t' + str(newjzc)
        syjl = gxfz.readlines()
        zxjl = syjl[-1].split()
        newzc = int(zxjl[1]) + int(sr) - int(zc)
        newfz = int(zxjl[2]) + int(yc) - int(ys)
        newjzc = newzc - newfz
        newfzb = '\n' + time.strftime('%Y-%m-%d', time.localtime()) + '\t' + str(newzc) + '\t' + str(newfz) + '\t' + str(newjzc)
        gxfz.write(newfzb)
def cz():
    while True:
        c = raw_input('\t查账模式\n1.查询最近十笔交易记录\n2.查询与某公司交易往来\n3.查询最近资产负债状况\n请选择查询内容：')
        if c.isdigit():
            c=int(c)
            if c==1:
                cz_jl(lszd)
                return False
            elif c==2:
                cz_gs(lszd)
                return False
            elif c==3:
                cz_fz(zcfzb)
                return False
            else:
                print '输入选择数字1/2/3'
                continue
        else:
            print '输入错误!!'

def main():
    while True:
        print("1.查账；2.记账；3.退出程序")
        service_id = raw_input("请选择服务：")
        if service_id.strip():
            service_id = service_id.strip()
            if service_id == "1" or service_id == "2" or service_id == "3":
                break
            else:
                print("请输入正确的服务类型（1 查账；2 记账；3 退出程序）")
            if service_id == "1":
                cz()
            elif service_id == "2":
                jz(lszd,zcfzb)
            elif service_id == "3":
                return False
        else:
            print ("请输入正确的服务类型（1 查账；2 记账；3 退出程序）")
main()