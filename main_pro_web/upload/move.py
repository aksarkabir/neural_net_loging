import os
import time

while 1:
    time.sleep(1)
    dir = os.listdir('/var/www/html/main_pro/upload/')

    hi = 'jj'

    for z in range(len(dir)):
        if dir[z].find('.txt')==-1:
            if dir[z].find('.py')==-1:
                hi = dir[z]
                break;
    if hi!='jj':
        a = 'mv '+hi+' test.jpg'
        os.system(a)
        a = 'mv test.jpg /home/kabir/codes/python/face/main_pro/data/'
        os.system(a)
    else:
        print "can't find any images"
