#coding:gbk
import pickle
test_data=['Save me!',123.456,True]
f=open(r'E:\OPS\技术\pylearn\crossin\test.data','w')
pickle.dump(test_data,f)
f.close()

