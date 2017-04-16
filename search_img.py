 # -*- coding:utf-8 -*-
import cv2
import os
import sys
import shutil
import time
from face import DBConnect
from face import FaceAPI
# outer_id="141402060900"

reload(sys)
sys.setdefaultencoding('utf8')
conn = DBConnect.dbconnect()
cur = conn.cursor()

if not os.path.exists("./data/log/search_img.log"):
	os.mknod('./data/log/search_img.log')

def main():
	global i,filesdir
	fileList=filelist('./data/search_img/')
	with open('./data/log/search_img.log','r') as f:
		content=f.read()
	for i in fileList:
		if i in content:
			filesdir=i.split('/')[3]
			print"{}:-----------Has Been exist!".format(filesdir)
		if i not in content:
			filesdir1=i.split('/')[3]
			filesdir=i.split('/')[3].split('.')[0]
			if not os.path.exists('./data/search_img/{}'.format(filesdir)):
				os.makedirs('./data/search_img/{}/'.format(filesdir))
				shutil.copyfile('./data/search_img/{}'.format(filesdir1),'./data/search_img/{}/{}'.format(filesdir,filesdir1))
			detect(i)
			with open("./data/log/search_img.log",'a') as f:
				f.write(i)
def filelist(dir,topdown=True):
	fileList = [] 
 	for root, dirs, files in os.walk(dir, topdown):
		for PicName in files:
			fileList.append(os.path.join(root,PicName))
		return fileList

def get_detail():
	cur.execute("select * from face_data where face_token='%s'"%face_token)
	line=cur.fetchone()
	ID,name,gender=line[0],line[1],line[3]
	detail=[ID,name]
	print"ID：{}".format(ID)
	print"Name：{}".format(name)
	print"gender：{}".format(gender)
	return detail
def detect(filename):
	global face_token
	count=0
	faces=[]
	face_cascade1 = cv2.CascadeClassifier('./data/cascades/haarcascade_frontalface_alt.xml')
	face_cascade2=cv2.CascadeClassifier('./data/cascades/haarcascade_frontalface_default.xml')
	img = cv2.imread(filename)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces1=face_cascade1.detectMultiScale(gray, 1.3, 5)
	faces2=face_cascade2.detectMultiScale(gray,1.3,5)
	try:
		faces=faces1 if faces1.size <= faces2.size else faces2
	except AttributeError:
		print"HEllO"

	ft=cv2.freetype.createFreeType2()
	ft.loadFontData(fontFileName='./data/font/simhei.ttf',id =0)

	for (x,y,w,h) in faces:
		img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
		f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
		cv2.imwrite('./data/search_img/{}/{}.pgm'.format(filesdir,time.strftime('%Y%m%d%H%M%S')), f)
		result=FaceAPI.searchItoI(image_file='./data/search_img/{}/{}.pgm'.format(filesdir,time.strftime('%Y%m%d%H%M%S')))
		if len(result)==4:
			break
		if result["results"][0]["confidence"] >= 80.00:
			print result["results"][0]["confidence"]
			face_token=result["results"][0]["face_token"]
			print"face_token：{}".format(face_token)
			detail=get_detail()
			# if not os.path.exists('./data/at/{}/{}.pgm'.format(detail[0],filesdir)):
				# shutil.copyfile("./data/search_img/{}/{}.pgm".format(filesdir,time.strftime('%Y%m%d%H%M%S')),"./data/at/%s/%s.pgm"%(detail[0],filesdir))
			ft.putText(img=img,text=detail[1], org=(x, y - 10), fontHeight=30,line_type=cv2.LINE_AA, color=(0,255,165), thickness=1, bottomLeftOrigin=True)
		else:
			print"Unknow face"
			cv2.putText(img,"Unknow", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,225), 2)
		count+=1
	cv2.imwrite(i,img)
if __name__ == '__main__':
	main()
	print "have done!"