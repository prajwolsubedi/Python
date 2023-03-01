# choice = '''Enter a Choice:
# 0: add  2: mul
# 1: sub  3: div

# '''

# print(choice)


#mutable and immutable 

# number = [100]
# print(id(number))
# number[0]=200
# print(id(number))

# string = 'abc'
# string[0] = z yesto garnu mildaina
# string 'zyx'

string = input('Enter any string ')
count = 0
for char in string:
    if(char == 'a'):
        count = count + 1

print(count)

counter = 0
while(counter<len(string)):
    if(counter=='a'):
        counter+=1
print(counter)