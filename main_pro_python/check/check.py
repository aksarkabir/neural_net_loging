import simplejson as sj
import os
import layer as l
import vector_data as v
import random

arr = v.vec_data('/home/kabir/codes/python/face/main_pro/check/test.jpg')

if len(arr)!=0:
    cn = 0

    fo = open('/home/kabir/codes/python/face/main_pro/data/data.txt', 'r')
    brr = sj.loads(fo.read())
    crr = brr['name']
    fo.close()

    for z in range(len(crr)):

        dir = '/home/kabir/codes/python/face/main_pro/data/'+crr[z]+'/data.txt'
        fo = open(dir, 'r')
        net = sj.loads(fo.read())
        fo.close()

        aaa = l.feed(net,arr)

        if aaa[0]>=.5:
            print crr[z], 'match', aaa[0]
            cn+=1
            num_dir = '/home/kabir/codes/python/face/main_pro/data/'+crr[z]+'/num.txt'
            f = open(num_dir,'r')
            num = sj.loads(f.read())
            f.close()
            randpass = random.randrange(1000,9999)
            f = open('/var/www/html/main_pro/data.txt','r')
            online_data = sj.loads(f.read())
            online_data['active']=1
            online_data['name'] = crr[z]
            online_data['num'] = num
            online_data['pass'] = str(randpass)
            f.close()
            f = open('/var/www/html/main_pro/data.txt','w')
            sj.dump(online_data,f)
            f.close()
            break
    if cn ==0:
        print 'no match found',arr[0]
        f = open('/var/www/html/main_pro/data.txt','r')
        online_data = sj.loads(f.read())
        online_data['active']=3
        f.close()
        f = open('/var/www/html/main_pro/data.txt','w')
        sj.dump(online_data,f)
        f.close()
else:
    print 'no face found'
    f = open('/var/www/html/main_pro/data.txt','r')
    online_data = sj.loads(f.read())
    online_data['active']=4
    f.close()
    f = open('/var/www/html/main_pro/data.txt','w')
    sj.dump(online_data,f)
    f.close()


fo = open('/home/kabir/codes/python/face/main_pro/check/data.txt', 'r')
crr = sj.loads(fo.read())
fo.close()
crr+=1
tt = 'mv test.jpg /home/kabir/codes/python/face/main_pro/check/trs/test'+str(crr)+'.jpg'
os.system(tt)
fo = open('/home/kabir/codes/python/face/main_pro/check/data.txt', 'w')
sj.dump(crr,fo)
fo.close()
