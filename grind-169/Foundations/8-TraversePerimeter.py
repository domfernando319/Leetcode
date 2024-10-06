def traversePerimeter(matrix):
    if not matrix or not matrix[0]:  # Check for empty matrix
        return []

    ROWS = len(matrix)
    COLS = len(matrix[0])
    perimeter = []

    # Top row
    for c in range(COLS):
        perimeter.append(matrix[0][c])

    # Right column (excluding the top and bottom corners)
    for r in range(1, ROWS - 1):
        perimeter.append(matrix[r][COLS - 1])

    # Bottom row (if there's more than one row)
    if ROWS > 1:
        for c in range(COLS - 1, -1, -1):
            perimeter.append(matrix[ROWS - 1][c])

    # Left column (excluding the top and bottom corners, if there's more than one column)
    if COLS > 1:
        for r in range(ROWS - 2, 0, -1):
            perimeter.append(matrix[r][0])

    return perimeter

mat1 = [
    [],
    [],
    [],
    []
]
mat2 = [
    [1, 2, 3, 4],
    [12, 0, 0, 5],
    [11, 0, 0, 6],
    [10, 9, 8, 7]
]
print(traversePerimeter(mat1))
print("#######################")
print(traversePerimeter(mat2))