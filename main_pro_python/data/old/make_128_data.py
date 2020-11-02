import os
import face_recognition_models as fm
import dlib
import skimage as sk
import numpy as np
import cv2 as cv
import csv
import simplejson as sj

f = open('/var/www/html/main_pro/upload/data.txt','r')
data = sj.loads(f.read())
f.close()

fo = open('data.txt', 'r')
brr = sj.loads(fo.read())
fo.close()

a = data['name']
b = data['number']

mdl = fm.pose_predictor_model_location()

frm = fm.face_recognition_model_location()

cnn = dlib.face_recognition_model_v1(frm)

fd = dlib.get_frontal_face_detector()

im = cv.imread('test.jpg')

hi = (200,200)

im = cv.resize(im, hi, interpolation = cv.INTER_AREA)
df = fd(im,1)

if len(df)!=0:
    mk = 'mkdir '+a
    os.system(mk)
    fpose = dlib.shape_predictor(mdl)
    pl = fpose(im,df[0])
    vec = cnn.compute_face_descriptor(im,pl)
    arr = []
    for z in range(len(vec)):
        arr.append(vec[z])
    dir = a+'/data.txt'
    fo = open(dir, 'w')
    sj.dump(arr,fo)
    fo.close()
    dir = a+'/num.txt'
    f = open(dir,'w')
    sj.dump(b,f)
    f.close()
    # fo = open('data.txt', 'r')
    # arr = sj.loads(fo.read())
    # arr.append(a)
    # fo.close()
    brr['name'].append(a)
    # fo = open('data.txt', 'w')
    # sj.dump(arr,fo)
    # fo.close()
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
