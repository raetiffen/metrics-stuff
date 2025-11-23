"""
    Rae Tiffen

    A ridge regression algorithm which inverts (X'X + lambda*I) directly by recursively applying the block matrix inverse formula

    Outputs a list of estimated coefficients from inputs y, X
"""

y = [[1,2,5,3,7,2,9]]
X = [[1,1,1,1,1,1,1],[1,2,3,4,5,6,7],[4,3,2,1,0,9,8],[6,2,5,8,9,2,5],[8,5,2,7,4,2,5]]
lmb = 0.5

def ridge(y,X):
    XtX = matmult(transpose(X),X)
    Xty = matmult(transpose(X),y)
    for i in range(len(XtX)):
        XtX[i][i] += lmb
    beta = matmult(block_inverse(XtX),Xty)
    return transpose(beta)[0]

def block_inverse(M):
    if len(M) == 1:
        return [[(M[0][0])**(-1)]]
    A = [[M[i][j] for j in range(len(M[0])-1)] for i in range(len(M)-1)]
    b = [[M[i][-1]] for i in range(len(M)-1)]
    c = [[M[-1][j] for j in range(len(M[0])-1)]]
    d = [[M[-1][-1]]]
    Ainv = block_inverse(A)
    Sinv = [[matadd(d,scalarmult(matmult(matmult(c,Ainv),b),-1))[0][0]**(-1)]]
    top_left = matadd(Ainv, scalarmult(matmult(matmult(Ainv,b),matmult(c,Ainv)), Sinv[0][0]))
    top_right = scalarmult(matmult(Ainv,b),-Sinv[0][0])
    bottom_left = scalarmult(matmult(c,Ainv),-Sinv[0][0])
    Minv = []
    for i in range(len(top_left)):
        Minv.append(top_left[i] + top_right[i])
    Minv.append(bottom_left[0] + Sinv[0])
    return Minv

def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

def scalarmult(A,c):
    return [[c*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matmult(A,B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]

def matadd(A,B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

if __name__== "__main__":
    print(ridge(transpose(y),transpose(X)))