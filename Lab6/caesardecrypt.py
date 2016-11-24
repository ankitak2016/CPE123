plain = ""
cipher ="Xlmw mw syv jmvwx mrtyx"
key = "E"
caesar_key = ord(key) - 65
ciphernum = 0
for i in cipher:
    ascii_value = ord(i)
    if(ascii_value>=65 and ascii_value<=90):
        changednum = ascii_value - 64
        ciphernum = (changednum - caesar_key)%26
        if(ciphernum==0):
            plain = plain + chr(90)
        else:
            plain = plain + chr(ciphernum+64)
    elif(ascii_value>=97 and ascii_value<=122):
        changednum = ascii_value - 96
        ciphernum = (changednum - caesar_key)%26
        if(ciphernum==0):
            plain = plain + chr(122)
        else:
            plain = plain + chr(ciphernum+96)
    else:
        plain = plain + i
print plain
