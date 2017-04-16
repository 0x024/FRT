# -*- coding:utf-8 -*-
import cv2
import time
import os
import sys
import shutil
import numpy as np
from face import FaceAPI
from face import DBConnect
# outer_id="141402060900"

reload(sys)
sys.setdefaultencoding('utf8')
conn = DBConnect.dbconnect()
cur = conn.cursor()
def normalize(X, low, high, dtype=None):
    X = np.asarray(X)
    minX, maxX = np.min(X), np.max(X)
    X = X - float(minX)
    X = X / float((maxX - minX))
    X = X * (high-low)
    X = X + low
    if dtype is None:
        return np.asarray(X)
    return np.asarray(X, dtype=dtype)
def read_images(sz=None):
    path="./data/at/"
    c = 0
    X,y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    if (filename == ".directory"):
                        continue
                    filepath = os.path.join(subject_path, filename)
                    im = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
                    if (sz is not None):
                        im = cv2.resize(im, (200, 200))
                    X.append(np.asarray(im, dtype=np.uint8))
                    y.append(c)
                except IOError, (errno, strerror):
                    print "I/O error({0}): {1}".format(errno, strerror)
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    raise
            c = c+1  
    return [X,y]

def get_detail():
    cur.execute("select * from face_data where face_token='%s'"%db_face_token)
    line=cur.fetchone()
    ID,name,gender=line[0],line[1],line[3]
    detail=[ID,name]
    return detail
def video():
    global db_face_token
    count = 0
    names = ['141402060901','141402060902','141402060903','141402060904','141402060905',
            '141402060906','141402060907','141402060908','141402060909',
            '141402060910','141402060911','141402060912','141402060913',
            '141402060914','141402060915','141402060916','141402060917',
            '141402060918','141402060919','141402060920','141402060921',
            '141402060922','141402060923','141402060924','141402060925',
            '141402060926','141402060927','141402060928','141402060929',
            '141402060930','141402060931','141402060932','141402060933']
    [X,y] = read_images()
    y = np.asarray(y, dtype=np.int32)
    model = cv2.face.createLBPHFaceRecognizer()
    ft=cv2.freetype.createFreeType2()
    ft.loadFontData(fontFileName='./data/font/simhei.ttf',id =0)
    # model = cv2.face.createEigenFaceRecognizer()
    model.train(np.asarray(X), np.asarray(y))   
    camera=cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('./data/cascades/haarcascade_frontalface_default.xml')


    while(True):
        read,img=camera.read()
        faces=face_cascade.detectMultiScale(img,1.3,5)

        if (count%20)<1:
            for(x,y,w,h) in faces:
                img =cv2.rectangle(img,(x,y),(x+w,y+h),(255,245,0),2)
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                f=cv2.resize(gray[y:y+h,x:x+w],(200,200))
                cv2.imwrite('./data/temp/temp.pgm',f)
                result=FaceAPI.searchItoI(image_file='./data/temp/temp.pgm')
                if len(result)==4:
                    break
                db_face_token=result["results"][0]["face_token"]
                detail=get_detail()
                # shutil.copyfile("./data/temp/temp.pgm","./data/at/%s/%s.pgm"%(detail,time.strftime('%Y%m%d%H%M%S')))
                print detail
                ft.putText(img=img,text=detail[1], org=(x, y - 10), fontHeight=60,line_type=cv2.LINE_AA, color=(0,255,165), thickness=2, bottomLeftOrigin=True)
                count+=1
        else:
            for (x, y, w, h) in faces:
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                roi=gray[x:x+w,y:y+h]
                try:
                    roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)
                    print roi.shape 
                    params = model.predict(roi)
                    print "Label: %s, Confidence: %.2f" % (params[0], params[1])
                    # ft.putText(img=img, text=names[params[0]-1], org=(x, y - 20), line_type=cv2.LINE_AA, color=(0,255,255), thickness=2,bottomLeftOrigin=True)
                    cv2.putText(img, names[params[0]-1], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
       
                    if (params[0] == 0):
                        cv2.imwrite('face_rec.jpg', img)
                except:
                    continue
            count+=1
        cv2.namedWindow("camera",cv2.WINDOW_NORMAL);  
        cv2.imshow("camera",img)
        if cv2.waitKey(1000 / 12)&0xff==ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    video() 