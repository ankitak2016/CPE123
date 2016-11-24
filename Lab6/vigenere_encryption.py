def main():
    plain_text = "WILL THIS ENCRYPTION WORK?"
    key = "crypto"
    numkeychar = 0
    finalcipher = ""
    for a in plain_text:
        finalcipher = finalcipher + caesar_encrypt(a,key[numkeychar])
        if(a == ' '):
            continue
        numkeychar=numkeychar+1
        if(numkeychar==len(key)):
            numkeychar = 0
    print finalcipher
def caesar_encrypt(plain,key):
    cipher=""
    if(ord(key)>=65 and ord(key)<=90):
        caesar_key = ord(key) - 65
    else:
        caesar_key = ord(key)-97
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
    return cipher
main()
