#write a python program to get the second largest number from a list

list = [9,10,3,20,20]

def find_second_maximum(list1):
    first_max = list1[0]
    second_max = list1[1]

    for i in range (2,len(list1)):
        if(list1[i] > first_max):
            second_max = first_max
            first_max = list1[i]
        elif list1[i] > second_max and list[i] != first_max:
            second_max = list1[i]
    return second_max

result = find_second_maximum(list)
print(result)



# nums.sort()
# print("Second largest number is ", nums[-2])


        