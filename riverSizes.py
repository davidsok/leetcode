from io import RawIOBase


def riverSizes(matrix):
    sizes = []
    rows = len(matrix)
    cols = len(matrix[0])
    visited = list()

    def visit(m,n):
        if m > -1 and m < rows and n > -1 and n < cols and matrix[m][n] == 1:
            matrix[m][n] = 0
            return 1 + visit(m,n-1) + visit(m-1,n) + visit(m,n+1) + visit(m+1,n)
        return 0

    for m in range(rows):
        for n in range(cols):
            if matrix[m][n] == 0:
                continue
            sizes.append(visit(m,n))
    print(matrix)
    return sizes

matrix = [
    [1,0,0,1,0],
    [1,0,1,0,0],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,1,0]
]
print(riverSizes(matrix))