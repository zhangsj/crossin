#coding:utf-8
import os
# for path,dirnames,filenames in os.walk(f):
def findfile(key,inputdir='.'):
    found_list=[]
    for path,dirnames,filenames in os.walk(inputdir):
        print 'searching',path,'...'
        for name in filenames:
            full_name=path+'/'+name
            if key in name:
                found_list.append(full_name)
            with open(full_name) as f:
                for l in f.readlines():
                    if key in l:
                        found_list.append(full_name + ':'+ l)
    return found_list
keyword=raw_input('search:')
path=raw_input('in:')
# print path
# print path.strip()
if not path.strip():
    path='.'
result=findfile(keyword,path)
print result
print '\n============== result ============\n\n'
for r in result:
    print r