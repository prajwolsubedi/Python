#write a python program to remove duplicates from a list

list = [1,2,3,4,5,6,6,7,7,8,8,4]

def remove_duplicate(list):
    noduplist = []
    for element in list:
        if element not in noduplist:
            noduplist.append(element)
    return noduplist


result = remove_duplicate(list)
print(result)
