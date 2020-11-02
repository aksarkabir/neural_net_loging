import face_recognition_models as fm
import dlib
import cv2 as cv
import numpy as np

def vec_data(path):
    mdl = fm.pose_predictor_model_location()

    frm = fm.face_recognition_model_location()

    cnn = dlib.face_recognition_model_v1(frm)

    fd = dlib.get_frontal_face_detector()

    im = cv.imread(path)

    hi = (200,200)

    im = cv.resize(im, hi, interpolation = cv.INTER_AREA)
    df = fd(im,1)
    a = []
    if len(df)!=0:
        fpose = dlib.shape_predictor(mdl)
        pl = fpose(im,df[0])
        vec = cnn.compute_face_descriptor(im,pl)
        for z in range(len(vec)):
            a.append(vec[z])
        return a
    else:
        return a
def dis(a,b):
    arr = np.array(a)
    brr = np.array(b)
    return np.linalg.norm(arr - brr, axis=0)
