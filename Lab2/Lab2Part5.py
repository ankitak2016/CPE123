f=open("bumps_on_a_log_2.txt")
fileline = f.readline()
power = -1
p=0
currentcount = 0
finalflag=""
for a in fileline:
    if(p==currentcount):
        print a
        finalflag=finalflag+a
        power = power +1
        currentcount = currentcount + 2**power + 1
    p=p+1
print finalflag
f.close()
quit()

