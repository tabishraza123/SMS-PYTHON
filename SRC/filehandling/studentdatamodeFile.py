
import json
import datetime



path=r"C:\pythoncode\SRC\filehandling"

student={}

student["id"]=int(input("please enter student's id :"))
student["name"]=input("please enter student's name :")
student["contact"]=int(input("please enter student's contact :"))
student["registration"]=datetime.datetime.now().strftime("%d-%m-%Y,%H.%M.%S")

output=json.dumps(student,indent=4)

with open(path,"a") as fa:
    fa.write(f"\n{output}")

with open(path,"r") as fr:
    print(fr.read())


    