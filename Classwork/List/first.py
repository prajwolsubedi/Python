l1 = ["prajwol", "pratyush", "Sahin", "Srijan", "Adidtya",1,2]


# string = "prajwol"
# print(string.reverse())

def reverse_function(x):
  return x[::-1]

new_list = []
for word in l1:
    if (word == type(str)):
       result = word.reversed()
       new_list.append(result)
    else:
       new_list.append(word)
    

print(new_list)




