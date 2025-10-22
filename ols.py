"""
    Rae Tiffen
    A minimal OLS algorithm using Modified Gram-Schmidt

    Outputs a list of estimates from inputs y, X
"""

y = [1,2,5,3,7,2,9]
X = [[1,1,1,1,1,1,1],[1,2,3,4,5,6,7],[4,3,2,1,0,9,8],[6,2,5,8,9,2,5],[8,5,2,7,4,2,5]]

def ols(y,X):
    return backsub(mgs(y,X))

def mgs(y,X):
    X.insert(0,y)
    n = len(X[0])
    R = {i: [] for i in range(len(X)-1)}
    for p in reversed(range(len(X))):
        for j in range(p):
            c = sum(X[p][i]*X[j][i] for i in range(n)) / sum(i**2 for i in X[p])
            R[p-1].append(c)
            X[j] = list(X[j][i] - X[p][i]*c for i in range(n))
    return R

def backsub(R):
    coeffs = []
    p = len(R)
    for i in range(p):
        b = R[i][0]
        for j in range(len(R[i])-1):
            b -= R[i][j+1]*coeffs[j]
        coeffs.append(b)
    return coeffs
    
if __name__== "__main__":
    print(ols(y,X))
