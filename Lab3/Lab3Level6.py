import hashlib
numberofattempts = 0
f = open("words.txt")
user_6_hashed_pass="963e37b615e688c9fcb696a9b20d5db1dfba2baa"
contents = f.readlines()
for line in contents:
    for n1 in range(1,9,1):
        for n2 in range(10):
            for n3 in range(10):
                level_6_pass = str(line.strip()+str(n1)+str(n2)+str(n3))
                user_guess_hashed = hashlib.sha1(level_6_pass).hexdigest()
                if(user_guess_hashed.strip()==user_6_hashed_pass.strip()):
                    break
                numberofattempts = numberofattempts+1
            if(user_guess_hashed.strip()==user_6_hashed_pass.strip()):
                break
        if(user_guess_hashed.strip()==user_6_hashed_pass.strip()):
            break
    if(user_guess_hashed.strip()==user_6_hashed_pass.strip()):
        break
print level_6_pass
print numberofattempts
