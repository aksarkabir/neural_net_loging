import simplejson as sj
import time
import os

while 1:
    time.sleep(1)
    f = open('/var/www/html/main_pro/data_extra.txt','r')
    arr = sj.loads(f.read())
    f.close()
    if arr['active']==1:
        fo = open('/home/kabir/codes/python/face/main_pro/data/data.txt','r')
        brr = sj.loads(fo.read())
        fo.close()
        brr['name'].remove(arr['name'])
        a = 'rm -R /home/kabir/codes/python/face/main_pro/data/'+arr['name']
        os.system(a)
        print 'done'
        arr['active']=0
        f = open('data_extra.txt','w')
        sj.dump(arr,f)
        f.close()
        f = open('/home/kabir/codes/python/face/main_pro/data/data.txt','w')
        sj.dump(brr,f)
        f.close()
    else:
        print 'nothing to delete'
