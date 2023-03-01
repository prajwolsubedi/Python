# use of range() to define a range of values
n = int (input("Enter no of rows"))

num = 1
for i in range(0,n):
    for j in range(0,i+1):
        result = chr(65+i+j)
        print(result,end=" ")
        num = num + 1
    print("\n")