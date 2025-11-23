"""
    Rae Tiffen

    No idea if this will work, but might as well try
"""

"""
    notes for writing:


    a row vector is a list
    a matrix is a list of row vectors
    so a column vector would be a list of single-entry lists
    if X is a matrix, X[i][j] gets the element in the ith row and jth column
    why am I not using numpy? because I'm trying to make this w/o any packages
"""

col = [[1], [2], [3], [4], [5]]
row = [[6, 7, 8, 9, 10]]
matA = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
"""
    let A be an m by n matrix
    len(A) is the number of rows
    len(A[0]) is the number of columns, assuming all rows have same number of entries (it must)

    # A m by n. m rows and n columns.
    # B n by p. n rows and p columns
    # Verify conformable?
    # For each row in the output. Then for each column in the output
    # There is a row in the output for each row in A
    # There is a column in the output for each column in B
    # Each entry is the dot product of row i of A with column j of B
"""

def matmult(A,B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


print(matmult(matA,col))
print(transpose(matA))