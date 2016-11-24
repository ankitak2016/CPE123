f=open("I_fibbed.txt")
filelines = f.readlines()
flag = ""
spacesbetween = 0
first = 0
second = 1
third = 0
p=0
finalflag=""
finalcount=0
for line in filelines:
    for a in line:
        if(p==finalcount):
            finalflag = finalflag+a
            if(p==0):
                pass
            elif(p==1):
                finalcount =finalcount+1
                pass
            else:
                third = first + second
                first = second
                second = third
             
            finalcount = finalcount + third +1      
        p=p+1

print finalflag
f.close()
quit()
