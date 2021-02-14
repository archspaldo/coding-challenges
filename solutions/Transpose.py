def transpose(matrix) :
    return list(list(x[i] for x in matrix) for i in range(len(matrix[0])))

print(transpose([[1,2,3], [4,5,6], [7,8,9]]))