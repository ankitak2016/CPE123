import hashlib
numberofattempts=0
f = open("words.txt")
user_3_hashed_pass="6108d30de651a14600a460621ea509c907c434da"
level_3_passfinal="none"
contents = f.readlines()
for line in contents:
    level_3_pass = line.strip()
    user_guess_hashed = hashlib.sha1(level_3_pass).hexdigest()
    if(user_3_hashed_pass.strip()==user_guess_hashed.strip()):
        level_3_passfinal = level_3_pass
        break
    numberofattempts = numberofattempts+1
print level_3_passfinal
print numberofattempts
