import string
import random
f=open("caesar_test.txt")
plaintext = ""
content = str(f.readline())
for i in range(65,90,1):
    key = chr(i)   
#def caesar_decrypt(cipher, key):
    plain = ""
	# Put your caesar decription here that maps cipher and key to plain text
	# Assume cipher is a string that could contain alphabetic, numeric, and punctuation
	# Upper case letters should map to upper case.  Lower case letters should map to lower case
	# Key is a single letter (for example "A")
	
    caesar_key = ord(key) - 64
    ciphernum = 0
    for i in content:
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
