list1 = [1,2,[3,4,[5,6,[7]],8,9],10]
list1[2][2][2][0] = 11
# print(list1[2][2][2][0])


A = [[1,2,3],
         [3,4,5],
         [6,7,8]]


C = [[1,2,3],
     [2,3,4]]
print(len(C))
print(len(C[0]))

B = [[1,2,3],
     [3,4,5],
     [6,7,8]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

for item in result:
    print(item)