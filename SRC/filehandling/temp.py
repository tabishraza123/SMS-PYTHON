
import json

path=r"C:\pythoncode\SRC\filehandling"
student={}

output=json.dumps(student,indent=4)


with open(path,"w") as fw:
    fw.write(f"\n{output}")

with open(path,"r") as fr:
    print(fr.read())




















#name=("my name is taique and i'm basically belongs to bihar i have done my graduation and in presence i'm doing web devlopment from indixpert and i want a success achievement  ")



    
    