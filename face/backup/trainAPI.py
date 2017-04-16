import os
import sys
import cv2
import numpy as np

def normalize(X, low, high, dtype=None):
    """Normalizes a given array in X to a value between low and high."""
    X = np.asarray(X)
    minX, maxX = np.min(X), np.max(X)
    # normalize to [0...1].
    X = X - float(minX)
    X = X / float((maxX - minX))
    # scale to [low...high].
    X = X * (high-low)
    X = X + low
    if dtype is None:
        return np.asarray(X)
    return np.asarray(X, dtype=dtype)


def read_images(sz=None):
    path="/home/ubuntu/Desktop/face-project/data/at"
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
                    # if (im is None):
                    #     print "image " + filepath + " is none"
                    # else:
                    #     print filepath
                    # resize to given size (if given)
                    if (sz is not None):
                        im = cv2.resize(im, (200, 200))

                    X.append(np.asarray(im, dtype=np.uint8))
                    y.append(c)
                except IOError, (errno, strerror):
                    print "I/O error({0}): {1}".format(errno, strerror)
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    raise
            # print c
            c = c+1
            

    print y
    return [X,y]

def face_rec(filename):
    names = ['141402060901','141402060902','141402060903'
    '141402060904','141402060905','141402060906','141402060907',
    '141402060908','141402060909','141402060910','141402060911',
    '141402060912','141402060913','141402060914','141402060915',
    '141402060916','141402060917','141402060918','141402060919',
    '141402060920','141402060921','141402060922','141402060923',
    '141402060924','141402060925','141402060926','141402060927',
    '141402060928','141402060929','141402060930','141402060931'
    '141402060932','141402060933']
    [X,y] = read_images()
    y = np.asarray(y, dtype=np.int32)
    model = cv2.face.createEigenFaceRecognizer()

    model.train(np.asarray(X), np.asarray(y))
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_alt.xml')
    img=cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi = gray[x:x+w, y:y+h]
        try:
            roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)
            # print roi.shape
            params = model.predict(roi)
            print "Label: %s, Confidence: %.2f" % (params[0], params[1])
            cv2.putText(img, names[params[0]], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
            if (params[0] == 0):
                cv2.imwrite('face_rec.jpg', img)
        except:
            continue
    # cv2.namedWindow(' Detected!!')
    # cv2.imshow('Vikings Detected!!', img)
    # cv2.imwrite('./vikings.jpg', img)
    # return names[params[0]]

# if __name__ == "__main__":
#     face_rec('./data/wenzhang1.jpg')

