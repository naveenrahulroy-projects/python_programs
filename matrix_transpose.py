matrix = [[1, 2], [3, 4]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
