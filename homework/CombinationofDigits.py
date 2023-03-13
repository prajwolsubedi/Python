#write a python program to print all possible combinations from the three digits

x,y,z = input("Enter any three numbers: \n").split()
list1 = []
list1.append(x)
list1.append(y)
list1.append(z)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
                print(list1[i],list1[j],list1[k])


