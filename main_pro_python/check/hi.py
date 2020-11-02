import os
import time

while 1:
    time.sleep(1)
    a = os.listdir('/home/kabir/codes/python/face/main_pro/check/')
    for z in range(len(a)):
        if a[z] == 'test.jpg':
            print 'running check.py'
            os.system('python check.py')
            break
    print 'running'
