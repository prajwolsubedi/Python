#write a python script that takes input from the user and displays that input back in lower case without using string function.

# Take input from the user
user_input = input("Enter a string: ")

# Convert the string to lowercase by subtracting 32 from ASCII value of each uppercase letter
lowercase_input = ""
for char in user_input:
    if ord(char) >= 65 and ord(char) <= 90:
        lowercase_input += chr(ord(char) + 32)
    else:
        lowercase_input += char

# Display the input in lowercase
print("Lowercase input:", lowercase_input)
