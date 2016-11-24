import hashlib
numberofattempts = 0
user_4_hashed_pass= "0449230bb53222d50b8404f08452ffde9ac4a4d5"
for a1 in range(65,90,1):
    for a2 in range(65,90,1):
        for a3 in range(65,90,1):
            for a4 in range(65,90,1):
                for a5 in range(65,90,1):
                    for a6 in range(65,90,1):
                        level_4_pass = str(chr(a1)+chr(a2)+chr(a3)+chr(a4)+chr(a5)+chr(a6))
                        user_guess_hashed = hashlib.sha1(level_4_pass).hexdigest()
                        if(user_4_hashed_pass.strip()==user_guess_hashed.strip()):
                            break
                        numberofattempts = numberofattempts + 1
                    if(user_4_hashed_pass.strip()==user_guess_hashed.strip()):
                        break
                if(user_4_hashed_pass.strip()==user_guess_hashed.strip()):
                    break
            if(user_4_hashed_pass.strip()==user_guess_hashed.strip()):
                break
        if(user_4_hashed_pass.strip()==user_guess_hashed.strip()):
            break                                    
    if(user_4_hashed_pass.strip()==user_guess_hashed.strip()):
        break
print level_4_pass
print numberofattempts 
                        
                    
