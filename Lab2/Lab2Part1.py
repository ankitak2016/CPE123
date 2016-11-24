import sys
f=open("hidden_in_plain_sight.txt")
filelines = f.readlines()
found_flag=False
closed_flag=False
flag = ""
for line in filelines:
    for i in line:
   	 if(i=="}"):
   		 closed_flag = True
   		 break
   	 if(i=="{"):
   		 found_flag=True
   	 elif(found_flag):
   		 flag = flag + i
   	 else:
   		 pass
    if(closed_flag):
   	 break
print flag
f.close()
quit()
