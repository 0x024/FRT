 # -*- coding:utf-8 -*-
import cv2
import datetime
import sys
import shutil
from face import FaceAPI
from face import DBConnect
# outer_id="141402060900"

reload(sys)
sys.setdefaultencoding('utf8')
conn = DBConnect.dbconnect()
cur = conn.cursor()
def get_detail():
	cur.execute("select * from face_data where face_token='%s'"%face_token)
	line=cur.fetchone()
	ID,name,gender=line[0],line[1],line[3]
	detail=[ID,name]
	print ID
	print name
	return detail
def video():
	global face_token
	ft=cv2.freetype.createFreeType2()
	ft.loadFontData(fontFileName='./data/font/simhei.ttf',id =0)
	face_cascade = cv2.CascadeClassifier('./data/cascades/haarcascade_frontalface_alt.xml')
	camera=cv2.VideoCapture(0)
	count = 0
	while(True):
		ret,frame=camera.read()
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		faces=face_cascade.detectMultiScale(gray,1.3,5)
		for(x,y,w,h) in faces:
			img =cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
			if count%10==1:

				f=cv2.resize(gray[y:y+h,x:x+w],(200,200))
				cv2.imwrite('./data/temp/temp.pgm',f)
				result=FaceAPI.searchItoI('./data/temp/temp.pgm')
				if len(result)==4:
					break			
				face_token=result["results"][0]["face_token"]
				detail=get_detail()
				confidence=result["results"][0]["confidence"]
				print confidence
				if confidence>=85.00:
					shutil.copyfile("./data/temp/temp.pgm","./data/at/%s/%s.pgm"%(detail[0],datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')))
				ft.putText(img=img,text=detail[1], org=(x, y - 10), fontHeight=60,line_type=cv2.LINE_AA, color=(0,255,165), thickness=2, bottomLeftOrigin=True)
				print count
			count +=1
		cv2.namedWindow("image",cv2.WINDOW_NORMAL)
		cv2.imshow("image",frame)
		if cv2.waitKey(1000 / 12)&0xff==ord("q"):
			break
	camera.release()
	cv2.destroyAllWindows()



if __name__ == '__main__':
	video() 
