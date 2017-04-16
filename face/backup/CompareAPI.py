import json
import os
from subprocess import Popen,PIPE 
def compare(face_token_1,face_token_2):
	global confidence
	result=Popen('curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/compare" -F \
		"api_key=sYVKydxGakOqX0tL-pw99CFI4WB1523s" -F \
		"api_secret=gCdp_hIlgdbnUhcvCv61znzOF53-32hA" -F \
		"face_token1=%s" -F \
		"face_token2=%s"'%(face_token_1,face_token_2),shell=True,stdout=PIPE)	
	wait=""	
	result=(result.stdout.read())
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/compare.json","w+")
	f.write(result)
	f.close()
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/compare.json")
	result=json.load(f)
	f.close()
	os.remove('/home/ubuntu/Desktop/face-project/faceAPI/log/compare.json')
	return result 
# if __name__ == '__main__':
# 	result=compareAPI('6635c06a425fc964ae5d14a959f3331e','abaab7aeefb818ad0f766ed3cc5d799b')
# 	confidence=result["confidence"]
# 	print"confidence:{}".format(confidence)