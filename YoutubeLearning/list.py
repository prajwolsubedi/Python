names = ["John", "Bob", "Mosh", "Lale", "kale",1,2.2]
names[4] = "Srijan"
# print(names[0])
# print(names[-1])
# print(names[-2])
# print(names)

#list methods
names.append("Pranim")

names.insert(0,"Sahin")
names.insert(-1,"Future")
print("San" in names)
print(len(names))
print(names)


#range() Function
#first is starting value and second is ending value and it is gonna be excluded and third value will be used as step
numbers = range(5,21,5)
print(numbers)
for num in range(5):
    print(num)

#list are mutable
#tuples in python they are immutable

numbers = (1,2,3)
print(numbers)


