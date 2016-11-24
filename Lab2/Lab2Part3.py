f=open("quad-radical.txt")
filelines = f.readlines()
spacesbetween = 0
square = 0
p=0
currentcount = 0
finalflag=""
intervalcount = -1
for line in filelines:
    for a in line:
        if(p==currentcount):
            finalflag=finalflag+a
            if(p==0):
                currentcount = currentcount + 1
            else:
                square = square +1
                currentcount = currentcount + (square*square) + 1
        p=p+1
print finalflag
f.close()
quit()
