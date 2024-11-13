# a python program to illustrate ceasar cipher technique
def encrypt(text, key):
	result=""
	for i in range (len(text)):
		char = text[i]
		if (char.isupper()):
			result += chr((ord(char) + key - 65) % 26 + 65)
		else:
			result += chr((ord(char) + key - 97) % 26 + 97)
	return result
text=str(input("Enter a string: "))
key=int(input("Enter a key: "))
print("Text : " +text)
print("Shift : " +str(key))
print("cipher : " +encrypt(text,key))
