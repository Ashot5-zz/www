def determinant(matrix):
    size = len(matrix)
    
    # If matrix is empty - return 1
    if not matrix or not matrix[0]:
        return 1

    # If matrix is 1x1 - return this element
    if size == 1:
        return matrix[0][0]

    # If matrix is 2x2 return fast determinant
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    total = 0
    for index in range(size):
        arr = [[value for row, value in enumerate(line) if row != index] for line in matrix[1:]]
        total += (-1) ** index * matrix[0][index] * determinant(arr)
    
    return total


if __name__ == '__main__':
    # Should return 1
    matrix = [[]]
    print(matrix, determinant(matrix))

    # Should return 7
    matrix = [[7]]
    print(matrix, determinant(matrix))

    # Should return -2
    matrix = [[1, 2], [3, 4]]
    print(matrix, determinant(matrix))

    # Should return 30
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, -1],
    ]
    print(matrix, determinant(matrix))

    # Should return 30
    matrix = [
        [3, 4, 6],
        [2, 3, -1],
        [9, 1, 1],
    ]
    print(matrix, determinant(matrix))

    # Should return -26
    matrix = [
        [2, 4, 1, 1],
        [0, 2, 1, 0],
        [2, 1, 1, 3],
        [4, 0, 2, 3]
    ]
    print(matrix, determinant(matrix))
