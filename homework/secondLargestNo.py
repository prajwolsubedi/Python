#write a python program to get the second largest number from a list

list = [6,2,3,4,5,7,8]
list2 = [1,2,3,4,5,6,7,8]

def find_third_maximum(list1):
    first_max = list1[0]
    second_max = list1[1]
    third_max = list1[2]

    for i in range (1,len(list1)):
        if(list1[i] > first_max):
            third_max = second_max 
            second_max = first_max
            first_max = list1[i]

        elif list1[i] > second_max and list1[i] != first_max:
            third_max = second_max
            second_max = list[i]
        elif list1[i] > third_max and list1[i] != second_max and list1[i] != first_max:
            third_max = list[i]


    return third_max

result = find_third_maximum(list)
print(result)




# nums.sort()
# print("Second largest number is ", nums[-3])


        