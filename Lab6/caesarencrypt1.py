plain = "This is our first input"
key = "E"
cipher = ""
caesar_key = ord(key) - 65
ciphernum = 0
for i in plain:
    ascii_value = ord(i)
    if(ascii_value>=65 and ascii_value<=90):
        changednum = ascii_value - 64
        ciphernum = (changednum + caesar_key)%26
        if(ciphernum==0):
            cipher = cipher + chr(90)
        else:
            cipher = cipher + chr(ciphernum+64)
    elif(ascii_value>=97 and ascii_value<=122):
        changednum = ascii_value - 96
        ciphernum = (changednum + caesar_key)%26
        if(ciphernum==0):
            cipher = cipher + chr(122)
        else:
            cipher = cipher + chr(ciphernum+96)
    else:
        cipher = cipher + i
print cipher
