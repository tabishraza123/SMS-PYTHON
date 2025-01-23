
#import json
#import datetime

path=r"C:\pythoncode\SRC\filehandling"
name=input("please enter your name ")

completepath=path +r"\\"+name
count=int(input("please enter total number of file :"))

for number in range(1,count+1):
    with open(f"{completepath}_{number}.txt","w") as fw:
        fw.write(f"this is tarique file number {number} ")

    

print(" Your file will be successfully created ")
