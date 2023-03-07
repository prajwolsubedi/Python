#write a python program to add "ing" at the end of a given string (length should be at least 3). If the given string already ends with "ing" add "ly" instead If the string length of the given string is less than 3 leave it unchanged.


string = input("Enter any string \n")


if(string[-3 : ] == "ing"):
    print(string + "ly")
elif(len(string) < 3):
    print(string)
else:
    print(string + "ing")

