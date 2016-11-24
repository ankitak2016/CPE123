
f=open("one_plus_one_equals_flag.txt")
filelines = f.readlines()
count = 0
p=0
currentcount = 0
finalflag=""
for line in filelines:
        for a in line:
            if(p==currentcount):
                 finalflag=finalflag+a
                 count = count +1
                 currentcount = currentcount+count
            p=p+1

print finalflag
f.close()
quit()
