"""
    Rae Tiffen

    Compares the recursive block inverse algorithm to numpy's linalg.inv function

    Runs both algorithms on random matrices from 2x2 to nxn, where below n=150. Outputs two plots, where the x-axis of both is the dimension of the invertied matrix:
        - Maximum difference (error) over all elements between the recursive block inverse and numpy inverse
        - Computation time of recursive block inverse and numpy inverse
    In my runs, the recursive block inverse increases in computation time roughly cubically as dimension increases.
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def test(n):
    # Runs tests from 2x2 to nxn
    max_errors = []
    times_numpy = []
    times_block = []
    for m in range(2,n+1):
        # make a random square matrix with numpy, tolist for block inverse
        # use an XtX-like matrix to ensure that the inverse block method works
        X = np.random.randint(-10,10, size=(m+100,m))
        mat = X.T @ X
        mat2 = mat.tolist()
        # run on numpy inverse, record time
        pren = time.time()
        minv1 = np.linalg.inv(mat)
        postn = time.time()
        times_numpy.append(postn-pren)
        # run on recursive block inverse, record time
        preb = time.time()
        minv2 = block_inverse(mat2)
        postb = time.time()
        times_block.append(postb-preb)
        # check difference, record highest-magnitude error
        diff = matadd(minv2,scalarmult(minv1.tolist(),-1))
        error = f"{max(max(abs(j) for j in i) for i in diff):.3e}"
        max_errors.append(error)
    # plot
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.plot(max_errors)
    plt.xlabel('Square matrix size minus two')
    plt.ylabel('Max difference between any element in numpy inv and block inv')
    
    plt.subplot(1,2,2)
    plt.plot(times_numpy, label="Numpy")
    plt.plot(times_block, label="Block")
    plt.xlabel('Square matrix size minus two')
    plt.ylabel('Computation time (seconds)')
    plt.legend()
    plt.tight_layout()
    plt.show()

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
    test(150)
