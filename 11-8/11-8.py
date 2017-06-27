#coding:utf-8

class jiangp:
    def __init__(self,guojia,jinp,yinp,tongp):
        self.guojia=guojia
        self.jinp=jinp
        self.yinp=yinp
        self.tongp=tongp
    def xz(self,mc):
        if mc==1:
            self.jinp+=1
        elif mc==2:
            self.yinp+=1
        elif mc==3:
            self.tongp+=1
        else:
            pass
    def zs(self):
        return self.jinp+self.yinp+self.tongp

    def info(self):
        return [self.guojia,self.jinp,self.yinp,self.tongp,self.zs()]

    # def __str__(self):
    #     return '%s: 金 %d, 银 %d, 铜 %d, 总 %d' % (self.guojia,self.jinp,self.yinp,self.tongp,self.zs())


if __name__=="__main__":
    china=jiangp("中国",30,20,10)
    us=jiangp("美国",20,20,10)
    # print china
    print "中国获得一枚银牌,美国获得一金一铜"
    china.xz(2)
    us.xz(1)
    us.xz(3)
    usinfo=us.info()
    chinainfo=china.info()
    zcj = [chinainfo, usinfo]
    # print chinainfo
    order_by_zs=sorted(zcj,key=lambda x:x[-1],reverse=True)
    for i in order_by_zs:
        print i[0],i[1],i[2],i[3],i[4]
    order_by_jinp=sorted(zcj,key=lambda x:x[0],reverse=True)
    for j in order_by_jinp:
        print j[0], j[1], j[2], j[3], j[4]

