import os
import json
from subprocess import Popen,PIPE
def detect(filename):
	result=Popen('curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/detect" -F \
		"api_key=sYVKydxGakOqX0tL-pw99CFI4WB1523s" -F \
		"api_secret=gCdp_hIlgdbnUhcvCv61znzOF53-32hA" -F \
		"image_file=@%s" -F \
		"return_attributes=gender,age,smiling,glass,headpose,facequality,blur" -F \
		"return_landmark=0"'%(filename),shell=True,stdout=PIPE)
	wait=""
	result=(result.stdout.read())
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/detect.json","w+")
	f.write(result)
	f.close()
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/detect.json")
	result=json.load(f)
	f.close()
	os.remove('/home/ubuntu/Desktop/face-project/faceAPI/log/detect.json')
	return result
# if __name__ == '__main__':
# 	result=detectAPI("../qimage.jpg")
# 	print result
