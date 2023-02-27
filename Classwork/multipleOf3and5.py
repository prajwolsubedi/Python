#Wap to list numbers which are multiple of 3 and 5 upto n terms
n = int (input("Enter the value of n: "))

for i in range(0,n):
    if(i % 3 == 0 and i % 5 == 0):
        print(i)


    
