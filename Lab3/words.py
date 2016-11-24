numberofattempts = 0
f = open("words.txt")
contents = f.readlines()
for line in contents:
    numberofattempts = numberofattempts +1
print numberofattempts
