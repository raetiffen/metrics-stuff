"""
    Rae Tiffen
    A minimal OLS algorithm using recursive FWL decompositions, defined in my thesis: https://scholarworks.uvm.edu/castheses/161/
    This is a heavily simplified version of the algorithm presented in: https://github.com/raetiffen/recursivefwl/blob/main/recursivefwl.py

    Outputs a list of estimates from inputs y, X
"""

y = [1,2,5,3,7,2,9]
X = [[1,1,1,1,1,1,1],[1,2,3,4,5,6,7],[4,3,2,1,0,9,8],[6,2,5,8,9,2,5],[8,5,2,7,4,2,5]]

def regress(y,x):
    coeff = sum(y[i]*x[i] for i in range(len(y))) / sum(i**2 for i in x)
    return coeff, [y[i] - x[i]*coeff for i in range(len(y))]

def recursive_fwl(y,X):
    if len(X) == 1:
        coeffs, resids = (regress(y,X[0]))
    else:
        coeffs = []
        for i in range(len(X)):
            c, resids = recursive_fwl(X[i],[X[j] for j in range(len(X)) if j != i])
            coeffs.append(regress(y,resids)[0])
        y_hat = [sum(coeffs[n] * X[n][i] for n in range(len(X))) for i in range(len(y))]
        resids = [y[i] - y_hat[i] for i in range(len(y))]
    return coeffs, resids
    
if __name__== "__main__":
    print(recursive_fwl(y,X)[0])
