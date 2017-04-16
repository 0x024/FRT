import os
import json
from subprocess import Popen,PIPE
def search(face_token_1,outer_id):
	result=Popen('curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/search" -F \
		"api_key=sYVKydxGakOqX0tL-pw99CFI4WB1523s" -F \
		"api_secret=gCdp_hIlgdbnUhcvCv61znzOF53-32hA" -F \
		"face_token=%s" -F \
		"outer_id=%s"'%(face_token_1,outer_id),shell=True,stdout=PIPE)	
	wait=""	
	result=(result.stdout.read())
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/search.json","w+")
	f.write(result)
	f.close()
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/search.json")
	result=json.load(f)
	f.close()
	os.remove('/home/ubuntu/Desktop/face-project/faceAPI/log/search.json')
	return result
# if __name__ == '__main__':
# 	resulr=searchAPI()