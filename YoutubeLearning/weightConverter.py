weight = float(input("Enter you weight \n"))

choice = input('''(K)g or (L)bs
''')

# if (choice == 'k' or choice == 'K'):
#     print("The Weight in pound is : ",weight*2.2046)
# elif(choice == 'L' or choice == 'l'):
#     print("The weight in kg is : ", weight * 0.45)
# else:
#     print("Wrong input")

if (choice.upper() == "K"):
    print("The Weight in pound is : ",weight*2.2046)
elif(choice.upper() == "L"):
    print("The weight in kg is : ", weight * 0.45)
else:
    print("Wrong input")


