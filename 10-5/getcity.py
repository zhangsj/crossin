import urllib2

url1 = 'http://m.weather.com.cn/data5/city.xml'
content1 = urllib2.urlopen(url1).read()
provinces = content1.split(',')
print provinces
result = 'city = {\n'
url = 'http://m.weather.com.cn/data5/city%s.xml'
for p in provinces:
    p_code = p.split('|')[0]
    url2 = url % p_code
    content2 = urllib2.urlopen(url2).read()
    cities = content2.split(',')
    for c in cities:
        c_code = c.split('|')[0]
        url3 = url % c_code
        content3 = urllib2.urlopen(url3).read()
        districts = content3.split(',')
        for d in districts:
            d_pair = d.split('|')
            d_code = d_pair[0]
            name = d_pair[1]
            url4 = url % d_code
            content4 = urllib2.urlopen(url4).read()
            print content4
            code = content4.split('|')[1]
            line = "    '%s': '%s',\n" % (name, code)
            result += line
            # print  name + ':' + code
result += '}'
f = file('getcityresult.py', 'w')
f.write(result)
f.close()