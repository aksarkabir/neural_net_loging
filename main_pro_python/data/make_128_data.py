import vector_data as v
import os
import simplejson as sj
import layer as l

f = open('/var/www/html/main_pro/upload/data.txt','r')
data = sj.loads(f.read())
f.close()

fo = open('data.txt', 'r')
brr = sj.loads(fo.read())
fo.close()

a = data['name']
b = data['number']

arr = v.vec_data('test.jpg')

if len(arr)!=0:
    f = open('im_data.txt','r')
    datax = sj.loads(f.read())
    f.close()

    for z in range(15):
        datax.append(arr)

    datay = []

    for z in range(30):
        if z<15:
            crr = [0]
            datay.append(crr)
        else:
            crr = [1]
            datay.append(crr)

    net = l.init_network(128,6,1)
    l.train(net,datax,datay,.1,1000)

    mk = 'mkdir '+a
    os.system(mk)

    dir = a+'/data.txt'
    fo = open(dir, 'w')
    sj.dump(net,fo)
    fo.close()

    dir = a+'/num.txt'
    f = open(dir,'w')
    sj.dump(b,f)
    f.close()

    brr['name'].append(a)

    data['active']=2
    f = open('/var/www/html/main_pro/upload/data.txt','w')
    sj.dump(data,f)
    f.close()

else:
    data['active']=3
    f = open('/var/www/html/main_pro/upload/data.txt','w')
    sj.dump(data,f)
    f.close()

brr['count']+=1
st = 'mv test.jpg '+'trs/test'+str(brr['count'])+'.jpg'
os.system(st)
f = open('data.txt', 'w')
sj.dump(brr,f)
f.close()
