
user_input = input("Enter any string: ")

lowercase_input = ""
for char in user_input:
    if ord(char) >= 65 and ord(char) <= 90:
        lowercase_input += chr(ord(char) + 32)
    else:
        lowercase_input += char

print("Lowercase: ",lowercase_input) 
