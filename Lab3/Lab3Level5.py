import hashlib
numberofattempts=0
user_5_hashed_pass="8b3a437b67f90a06248180dbcfa6637cce2db8ac"
for a1 in range(65,90,1):
    for a2 in range(65,90,1):
        for a3 in range(65,90,1):
            for n1 in range(1,9,1):
                for n2 in range(10):
                    for n3 in range(10):
                        level_5_pass = str(chr(a1)+chr(a2)+chr(a3)+str(n1)+str(n2)+str(n3))
                        user_guess_hashed = hashlib.sha1(level_5_pass).hexdigest()
                        if(user_guess_hashed.strip()==user_5_hashed_pass.strip()):
                            break
                        numberofattempts = numberofattempts+1
                    if(user_guess_hashed.strip()==user_5_hashed_pass.strip()):
                        break
                if(user_guess_hashed.strip()==user_5_hashed_pass.strip()):
                    break
            if(user_guess_hashed.strip()==user_5_hashed_pass.strip()):
                break
        if(user_guess_hashed.strip()==user_5_hashed_pass.strip()):
            break
    if(user_guess_hashed.strip()==user_5_hashed_pass.strip()):
        break
print level_5_pass
print numberofattempts
