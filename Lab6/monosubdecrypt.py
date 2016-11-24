key = "ISYVKJRUXEDZQMCTPLOFNBWGAH"
key2 = key.lower()
f = open("mono_test.txt")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = f.readline()
plaintext =""
for i in cipher:
	ascii_value = ord(i)
	if(ascii_value>=65 and ascii_value<=90):
		plaintext = plaintext+alphabet[key.index(i)]
	elif(ascii_value>=97 and ascii_value<=122):
		plaintext = plaintext + alphabet[key2.index(i)].lower()
	else:
		plaintext = plaintext + i
print plaintext

