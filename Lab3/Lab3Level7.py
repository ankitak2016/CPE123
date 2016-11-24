import hashlib
numberofattempts = 0
f = open("words.txt")
user_7_hashed_pass="3e24cffc76002cfd4c3871aac82537c153531775"
contents = f.readlines()
for line in contents:
    for n1 in range(1,9,1):
        for n2 in range(10):
            for n3 in range(10):
                for a1 in range(65,90,1):
                    level_7_pass = str(line.strip() + str(n1) + str(n2)+ str(n3) +str(chr(a1)))
                    user_guess_hashed = hashlib.sha1(level_7_pass).hexdigest()
                    if(user_guess_hashed.strip()==user_7_hashed_pass.strip()):
                        break
                    numberofattempts = numberofattempts+1
                if(user_guess_hashed.strip()==user_7_hashed_pass.strip()):
                    break
            if(user_guess_hashed.strip()==user_7_hashed_pass.strip()):
                break
        if(user_guess_hashed.strip()==user_7_hashed_pass.strip()):
            break
    if(user_guess_hashed.strip()==user_7_hashed_pass.strip()):
        break
print level_7_pass
print numberofattempts
