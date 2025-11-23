"""
    Rae Tiffen

    No idea if this will work, but might as well try

    Note: The input notation for this is different than my other OLS algorithms. X[i][j] is the element in the ith row and jth column of X. That is, X is a list of lists, where each list is a row (NOT a column). Below I use the same y and X as the other algorithms (where each list is a column/variable), I simply transpose them before inputting it into the OLS function.
"""

"""
    let A be an m by n matrix
    len(A) is the number of rows
    len(A[0]) is the number of columns, assuming all rows have same number of entries (it must)
    A[i][j] gets the element in the ith row and jth column
"""

y = [[1,2,5,3,7,2,9]]
X = [[1,1,1,1,1,1,1],[1,2,3,4,5,6,7],[4,3,2,1,0,9,8],[6,2,5,8,9,2,5],[8,5,2,7,4,2,5]]

def matmult(A,B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

def ols(y,X):
    XtX = matmult(transpose(X),X)
    Xty = matmult(transpose(X),y)
    beta = matmult(block_inverse(XtX),Xty)
    return beta

def block_inverse(A):
    return

if __name__== "__main__":
    print(ols(transpose(y),transpose(X)))