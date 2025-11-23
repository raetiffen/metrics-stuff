"""
    Rae Tiffen

    No idea if this will work, but might as well try

    Note: The input notation for this is different than my other OLS algorithms. Here, X[i][j] is the element in the ith row and jth column of X. That is, X is a list of lists, where each list is a row (in other algorithms it's a column). Below I use the same example y and X as in the other algorithms (where each list is a column/variable), I simply transpose them when calling the OLS function.
"""

"""
    let A be an m by n matrix
    len(A) is the number of rows
    len(A[0]) is the number of columns, assuming all rows have same number of entries (it must)
    A[i][j] gets the element in the ith row and jth column
"""

y = [[1,2,5,3,7,2,9]]
X = [[1,1,1,1,1,1,1],[1,2,3,4,5,6,7],[4,3,2,1,0,9,8],[6,2,5,8,9,2,5],[8,5,2,7,4,2,5]]

def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

def scalarmult(A,c):
    return [[c*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matmult(A,B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]

def matadd(A,B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def ols(y,X):
    XtX = matmult(transpose(X),X)
    Xty = matmult(transpose(X),y)
    beta = matmult(block_inverse(XtX),Xty)
    return beta

def block_inverse(M):
    # Base case: if M is 1x1, return M inverse
    if len(M) == 1: # and len(M[0]) == 1:
        return [[(M[0][0])**(-1)]]
    # Break apart M in to A, b, c, d
    A = [[M[i][j] for j in range(len(M[0])-1)] for i in range(len(M)-1)]
    b = [[M[i][-1]] for i in range(len(M)-1)]
    c = [[M[-1][j] for j in range(len(M[0])-1)]]
    d = [[M[-1][-1]]]
    # Recursive call goes here
    Ainv = block_inverse(A)
    # Get inverse schur complement
    Sinv = [[matadd(d,scalarmult(matmult(matmult(c,Ainv),b),-1))[0][0]**(-1)]]
    # Construct matrix to pass back up
    top_left = matadd(Ainv, scalarmult(matmult(matmult(Ainv,b),matmult(c,Ainv)), -Sinv[0][0]))
    top_right = scalarmult(matmult(Ainv,b),-Sinv[0][0])
    bottom_left = scalarmult(matmult(c,Ainv),-Sinv[0][0])
    bottom_right = Sinv

    return

if __name__== "__main__":
    print(ols(transpose(y),transpose(X)))