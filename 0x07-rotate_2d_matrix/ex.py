#!/usr/bin/python3

matrix = [
    [1, 5, 3, 4],
    [2, 6, 7, 8],
    [3, 7, 11, 12],
    [4, 8, 15, 16]
]

# transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(transpose)

# for i in range(len(matrix)):
#     matrix[i].reverse()
# 
# print(matrix)

reverse = [row[::-1] for row in matrix]
print(reverse)