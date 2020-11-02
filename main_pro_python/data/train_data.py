import os
import vector_data as v
import simplejson as sj
import layer as l

f = open('im_data.txt','r')

datax = sj.loads(f.read())

f.close()

arr = v.vec_data('test.jpg')

if len(arr)!=0:
    for z in range(15):
        datax.append(arr)

    datay = []
    for z in range(30):
        if z<15:
            arr = [0]
            datay.append(arr)
        else:
            arr = [1]
            datay.append(arr)

    net = l.init_network(128,6,1)
    l.train(net,datax,datay,.1,1000)
    f = open('shihab_data.txt','w')
    sj.dump(net,f)
    f.close()

else:
    print 'no face found'
