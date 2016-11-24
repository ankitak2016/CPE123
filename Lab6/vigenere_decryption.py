
def main():
    f = open("vigenere_test.txt")
    plaintext = f.readline()
    numkeychar = 0
    key = "turing"
    finalcipher = ""
    for a in plaintext:
        finalcipher = finalcipher + caesar_decrypt(a,key[numkeychar])
        if(not (ord(a)>=65 and ord(a)<=90 or ord(a)>=97 and ord(a)<=122)):
            continue
        numkeychar=numkeychar+1
        if(numkeychar==len(key)):
            numkeychar = 0
    print finalcipher
def caesar_decrypt(plain,key):
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
            ciphernum = (changednum - caesar_key)%26
            if(ciphernum==0):
                cipher = cipher + chr(90)
            else:
                cipher = cipher + chr(ciphernum+64)
        elif(ascii_value>=97 and ascii_value<=122):
            changednum = ascii_value - 96
            ciphernum = (changednum - caesar_key)%26
            if(ciphernum==0):
                cipher = cipher + chr(122)
            else:
                cipher = cipher + chr(ciphernum+96)
        else:
            cipher = cipher + i
    return cipher
main()
