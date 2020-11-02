import os
import face_recognition_models as fm
import dlib
import skimage as sk
import numpy as np
import cv2 as cv
import csv
import simplejson as sj
import face_recognition
import simplejson as sj
import socket
import random
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 5000))


mdl = fm.pose_predictor_model_location()

frm = fm.face_recognition_model_location()

cnn = dlib.face_recognition_model_v1(frm)

fd = dlib.get_frontal_face_detector()

im = cv.imread('test.jpg')

hi = (200,200)

im = cv.resize(im, hi, interpolation = cv.INTER_AREA)
df = fd(im,1)

if len(df)!=0:
    fpose = dlib.shape_predictor(mdl)
    pl = fpose(im,df[0])
    vec = cnn.compute_face_descriptor(im,pl)
    arr = np.array(vec)
    fo = open('/home/kabir/codes/python/face/main_pro/data/data.txt', 'r')
    brr = sj.loads(fo.read())
    crr = brr['name']
    fo.close()
    cn = 0
    for z in range(len(crr)):
        dir = '/home/kabir/codes/python/face/main_pro/data/'+crr[z]+'/data.txt'
        fo = open(dir, 'r')
        brr = sj.loads(fo.read())
        brr = np.array(brr)
        fo.close()
        aaa = np.linalg.norm(arr - brr, axis=0)
        print aaa
        if aaa<=.5:
            print crr[z], 'match', aaa
            cn+=1
            sock.send(crr[z])
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
        print 'no match found'
        f = open('/var/www/html/main_pro/data.txt','r')
        online_data = sj.loads(f.read())
        online_data['active']=3
        f.close()
        f = open('/var/www/html/main_pro/data.txt','w')
        sj.dump(online_data,f)
        f.close()
        sock.send('no match found')
else:
    print 'no face found'
    f = open('/var/www/html/main_pro/data.txt','r')
    online_data = sj.loads(f.read())
    online_data['active']=4
    f.close()
    f = open('/var/www/html/main_pro/data.txt','w')
    sj.dump(online_data,f)
    f.close()
    sock.send('no face found')
fo = open('data.txt', 'r')
crr = sj.loads(fo.read())
fo.close()
crr+=1
tt = 'mv test.jpg /home/kabir/codes/python/face/main_pro/check/trs/test'+str(crr)+'.jpg'
os.system(tt)
fo = open('data.txt', 'w')
sj.dump(crr,fo)
fo.close()
sock.close()
