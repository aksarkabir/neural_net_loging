import os
import time
import socket

while 1:
    a = os.listdir('/var/www/html/main_pro/')
    b = 'hi'
    time.sleep(1)
    for z in range(len(a)):
        if a[z].find('.html')==-1:
            if a[z].find('.php')==-1:
                if a[z].find('.py')==-1:
                    if a[z].find('.txt')==-1:
                        if a[z].find('.css')==-1:
                            if a[z].find('.js')==-1:
                                if a[z]!='upload':
                                    b = a[z]
                                    break



    if b != 'hi':
        # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.connect(('127.0.0.1', 5000))
        t = 'mv '+b+' test.jpg'
        tt = 'mv test.jpg /home/kabir/codes/python/face/main_pro/check/test.jpg'
        ttt = 'python /home/kabir/codes/python/face/main_pro/check/check.py'
        os.system(t)
        os.system(tt)
        # os.system(ttt)
        # sock.send('processing')
        # sock.close()
    else:
        print 'cant find any'
