# print(example[:3])

# reverse_word = ''
# for char in example:
#     reverse_word = char+reverse_word
#     print(char)

# print(reverse_word)
# print(example[::-1])

# example = "abcdef"
# length = len(example)


# new_word = input("Enter the word you want to insert")

# for char in example:
#     print(example[:3]+new_word+example)


print("Your no is {2} {1} {0}".format(1,2,3))
print("Your no is {second} {first}".format(first=1, second=2))

print("#".join(["as","xy"]))


print("abcdef".replace("ab","xy"))

print("ab,cd,ef".split(","))


# list is mutable and it allows dublication ex list1 = ["a","a"]
# string in imutable

list1 = ["a","a",45,50,"x"]
list1.append("y")
print(list1[3])