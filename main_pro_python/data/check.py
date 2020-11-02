import os
import time
import simplejson as sj

while 1:
    time.sleep(1)
    f = open('/var/www/html/main_pro/upload/data.txt','r')
    arr = sj.loads(f.read())
    f.close()

    if arr['active']==1:
        print 'found'
        f = open('/var/www/html/main_pro/upload/data.txt','w')
        arr['active']=99
        sj.dump(arr,f)
        f.close()
        os.system('python make_128_data.py')
    else:
        print 'not found'
