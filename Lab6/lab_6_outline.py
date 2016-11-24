import string
import random
def caesar_encrypt(plain, key):
#Put your caesar cipher here that maps plain and key to cipher
# Assume plain is a string that could contain alphabetic, numeric, and punctuation
# Upper case letters should map to upper case.  Lower case letters should map to lower case
# Key is a single letter (for example "A")
    cipher=""
    caesar_key=ord(key)-65
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
def caesar_decrypt(cipher, key):
	# Put your caesar decription here that maps cipher and key to plain text
	# Assume cipher is a string that could contain alphabetic, numeric, and punctuation
	# Upper case letters should map to upper case.  Lower case letters should map to lower case
	# Key is a single letter (for example "A")
	plain=""
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
	return plain	

def vigenere_encrypt(plain, key):
	# Assume plain is a string that could contain alphabetic, numeric, and punctuation
	# Upper case letters should map to upper case.  Lower case letters should map to lower case
	# Key is a string of letters of arbitraty size.  Ignore punctuation and numbers in the key.
	cipher = ""
	numkeychar = 0
	for a in plain:
		cipher = cipher + caesar_encrypt(a,key[numkeychar].upper())
		if(not (ord(a)>=65 and ord(a)<=90 or ord(a)>=97 and ord(a)<=122)):
			continue
		numkeychar=numkeychar+1
		if(numkeychar==len(key)):
			numkeychar = 0  
	return cipher
def vigenere_decrypt(cipher, key):
	# Assume cipher is a string that could contain alphabetic, numeric, and punctuation
	# Upper case letters should map to upper case.  Lower case letters should map to lower case
	# Key is a string of letters of arbitraty size.  Ignore punctuation and numbers in the key.  
	plain = ""
	numkeychar = 0
	for a in cipher:
		plain = plain + caesar_decrypt(a,key[numkeychar].upper())
		if(not (ord(a)>=65 and ord(a)<=90 or ord(a)>=97 and ord(a)<=122)):
			continue
		numkeychar=numkeychar+1
		if(numkeychar==len(key)):
			numkeychar = 0
	return plain
	
def monosub_encrypt(plain, key):
	cipher = ""
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in plain:
		ascii_value=ord(i)
		if(ascii_value>=65 and ascii_value<=90):
			cipher = cipher + key[alphabet.index(i)]
		elif(ascii_value>=97 and ascii_value<=122):
			cipher = cipher + key[alphabet.index(i.upper)].lower
		else:
			cipher = cipher + i
	# Assume plain is a string that could contain alphabetic, numeric, and punctuation
	# Upper case letters should map to upper case.  Lower case letters should map to lower case
	# Key is a string of letters 26 long.  Assume each letter only appears once 
	return cipher

def monosub_decrypt(cipher, key):
	# Assume plain is a string that could contain alphabetic, numeric, and punctuation
	# Upper case letters should map to upper case.  Lower case letters should map to lower case
	# Key is a string of letters 26 long.  Assume each letter only appears once 
	plain = ""
	keylower = key.lower()
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in cipher:
		ascii_value = ord(i)
		if(ascii_value>=65 and ascii_value<=90):
			plain = plain+alphabet[key.index(i)]
		elif(ascii_value>=97 and ascii_value<=122):
			plain = plain+ alphabet[keylower.index(i)].lower()
		else:
			plain = plain + i
	return plain

def key_gen():
	key = ""
	alphabet = ""
	# Key is a string of letters 26 long. 
	# Some functions that may help
	# random.sample
	# string.ascii_uppercase
	# ''.join()
	return key 

def chi_squared_test(text):
	score = 0
	alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	expdist = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
	totalchar = 0
	for i in range(0,25,1):
		numchar = 0
		totalchar = 0
		for ch in text:
			if(ch==' '):
				continue
			totalchar = totalchar+1
			if(alphabet[i]==ch or alphabet[i].lower()==ch):
				numchar = numchar+1
		E_i = expdist[i]*totalchar
		score = score + (((numchar-E_i)**2)/E_i)

	#Sum from i = A to Z of (C_i - E_i)^2/E_i.  Where C_A is the count (not probability) of A and E_A is the expected count of A
	# Expected distribution is [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]; 
	# Expected count is tot_letters * distribution
	return score

def expected_key(text):
	key = -1 # Sets the current best key to -1
	score = 10000000 # Sets the current score to a really high score
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in range(26): # Cycles through all the letters (0-25) In this loop test whether the score of the shift is better or worse then the current best score.  If it is better replace the key and score otherwise continue
		textenc = caesar_decrypt(text,alphabet[i])
		chiscore = chi_squared_test(textenc)	
		if(chiscore<score):	
			score = chiscore
			key = alphabet[i]
	return key, score
def decrypt_802():
	output_file = open("caesar_decrypted_YOUR_GROUP_NAME.txt", 'w') # Replace YOUR_GROUP_NAME with a name for your group
	for file_num in range(1, 802):
		filename = "CAESAR" + str(file_num) + ".txt"
		# in here put your code to get the text out of the file and put it in a string
		f=open(filename)
		contents = f.readline()
		key, score = expected_key(contents) # Find the key for the string.  Replace "" with your string 
		plain = caesar_decrypt(contents, key) # replace "" with your string
		output_file.write(str(ord(key)-65 + "," + str(score) + "," + plain + "\n") 
		# For CAESAR1.txt this should write 9, 20.55, IN ANOTHER MOMENT DOWN WENT ALICE AFTER IT  NEVER ONCE CONSIDERING HOW IN THE WORLD SHE WAS TO GET OUT AGAIN
def main():
	#Put your cases here
	#Including the following
	#Test your Caesar encryption, print the input and output to screen
	print "caesar_encrypt test"
	print caesar_encrypt("This is our first input","E")
	print ""
	#Test your Caesar decryption, print the input and input to screen
	print "caesar_decrypt test"
	print caesar_decrypt("Xlmw mw syv jmvwx mrtyx","E")
	print ""
	#Test your Vigenere encryption, print the input and output to screen
	print "vigenere_encrypt test"
	print vigenere_encrypt("WILL THIS ENCRYPTION WORK","crypto")
	print ""
	#Test your Vigenere decryption, print the input and input to screen
	print "vigenere_decrypt test"
	f = open("vigenere_test.txt")
	plaintext = f.readline()
	print vigenere_decrypt(plaintext,"turing")
	f.close()
	print ""
	#Test your mono encryption, print the input and output to screen
	#Test your mono decryption, print the input and input to screen
	print "monosub_decrypt test"
	key = "ISYVKJRUXEDZQMCTPLOFNBWGAH"
	f = open("mono_test.txt")
	cipher = f.readline()
	print monosub_decrypt(cipher,key)
	f.close()
	print ""
	pass
	#decrypt_802()

main()
