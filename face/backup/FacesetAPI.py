import json
import os
from subprocess import Popen,PIPE 
def facesetcreate(outer_id,face_tokens=None):
	global confidence
	result=Popen('curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/faceset/create" -F \
		"api_key=sYVKydxGakOqX0tL-pw99CFI4WB1523s" -F \
		"api_secret=gCdp_hIlgdbnUhcvCv61znzOF53-32hA" -F \
		"outer_id=%s" -F \
		"face_tokens=%s"'%(outer_id,face_tokens),shell=True,stdout=PIPE)	
	wait=""	
	result=(result.stdout.read())
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/facesetcreate.json","w+")
	f.write(result)
	f.close()
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/facesetcreate.json")
	result=json.load(f)
	f.close()
	os.remove('/home/ubuntu/Desktop/face-project/faceAPI/log/facesetcreate.json')
	return result 

def facesetaddface(outer_id,face_tokens):
	global confidence
	result=Popen('curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/faceset/addface" -F \
		"api_key=sYVKydxGakOqX0tL-pw99CFI4WB1523s" -F \
		"api_secret=gCdp_hIlgdbnUhcvCv61znzOF53-32hA" -F \
		"outer_id=%s" -F \
		"face_tokens=%s"'%(outer_id,face_tokens),shell=True,stdout=PIPE)	
	wait=""	
	result=(result.stdout.read())
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/facesetaddfacce.json","w+")
	f.write(result)
	f.close()
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/facesetaddfacce.json")
	result=json.load(f)
	f.close()
	print result
	os.remove('/home/ubuntu/Desktop/face-project/faceAPI/log/facesetaddfacce.json')
	return result 


def facesetremoveface(outer_id,face_tokens):
	global confidence
	result=Popen('curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/faces" -F \
		"api_key=sYVKydxGakOqX0tL-pw99CFI4WB1523s" -F \
		"api_secret=gCdp_hIlgdbnUhcvCv61znzOF53-32hA" -F \
		"outer_id=%s" -F \
		"face_tokens=%s"'%(outer_id,face_tokens),shell=True,stdout=PIPE)	
	wait=""	
	result=(result.stdout.read())
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/facesetremoveface.json","w+")
	f.write(result)
	f.close()
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/facesetremoveface.json")
	result=json.load(f)
	f.close()
	print result
	os.remove('/home/ubuntu/Desktop/face-project/faceAPI/log/facesetremoveface.json')
	return result 



def facesetgetdetail(outer_id):
	result=Popen('curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail" -F \
		"api_key=sYVKydxGakOqX0tL-pw99CFI4WB1523s" -F \
		"api_secret=gCdp_hIlgdbnUhcvCv61znzOF53-32hA" -F \
		"outer_id=%s"'%(outer_id),shell=True,stdout=PIPE)	
	wait=""	
	result=(result.stdout.read())
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/facesetgetdetail.json","w+")
	f.write(result)
	f.close()
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/facesetgetdetail.json")
	result=json.load(f)
	f.close()
	print result
	os.remove('/home/ubuntu/Desktop/face-project/faceAPI/log/facesetgetdetail.json')
	return result 


def facesetdelete(outer_id):
	global confidence
	result=Popen('curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/faceset/delete" -F \
		"api_key=sYVKydxGakOqX0tL-pw99CFI4WB1523s" -F \
		"api_secret=gCdp_hIlgdbnUhcvCv61znzOF53-32hA" -F \
		"check_empty=0" -F \
		"outer_id=%s"'%(outer_id),shell=True,stdout=PIPE)	
	wait=""	
	result=(result.stdout.read())
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/facesetdelete.json","w+")
	f.write(result)
	f.close()
	f=open("/home/ubuntu/Desktop/face-project/faceAPI/log/facesetdelete.json")
	result=json.load(f)
	f.close()
	print result
	os.remove('/home/ubuntu/Desktop/face-project/faceAPI/log/facesetdelete.json')
	return result 




# if __name__ == '__main__':
	# result=facesetcreate('1','cb0d7fcd227124046d1c782076abb8a5,7e1684935d0141f261378772683cb410')
	# print result

	# result=facesetgetdetail('1')
	# print result
	# confidence=result["confidence"]
	# print"confidence:{}".format(confidence)
	

	# result=facesetaddface("1","cae2e796ad38737a5006fde10b529c32")
	# print result
	# result=facesetdelete('1')
	# print result