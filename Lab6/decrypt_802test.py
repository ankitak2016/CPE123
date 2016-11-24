def decrypt_802():
	output_file = open("caesar_decrypted_AnkitaKoratkar_HannahKwang_CPE123.txt", 'w') # Replace YOUR_GROUP_NAME with a name for your group
	for file_num in range(1,6):
		filename = "CAESAR" + str(file_num) + ".txt"
		# in here put your code to get the text out of the file and put it in a string
		f=open(filename)
		contents = f.readline()
		key, score = expected_key(contents) # Find the key for the string.  Replace "" with your string 
		plain = caesar_decrypt(contents, key) # replace "" with your string
		output_file.write(str(ord(key)-65) + "," + str(score) + "," + plain + "\n")
def main():
	decrypt_802()
	pass
main()