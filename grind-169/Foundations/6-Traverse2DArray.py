def traverse2DArray(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    for r in range(ROWS):
        for c in range(COLS):
            print(matrix[r][c])
        print("###")

mat1 = [
    [1,0, 1,0],
    [0, 1, 1, 1],
    [1, 1, 0, 1]
]
mat2 = [
    [0,0,1,0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [1,1, 1, 1]
]
traverse2DArray(mat1)
print("#######################")
traverse2DArray(mat2)
