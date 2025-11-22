"""
    Rae Tiffen

    Cool curve generator
    Fits successive powers of t (a variable which iterates by 1 in each observation) to normally-distributed data, such that it is fit without error, and plots the resulting curve
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def perfect_fit(n):
    t = np.arange(1,n+1)
    y = np.random.normal(0, 2, n)
    X = np.vander(t, N=n, increasing=True)

    model = LinearRegression(fit_intercept=False).fit(X,y)
    tf = np.linspace(t.min(), t.max(), (n*10))
    Xf = np.vander(tf, N=n, increasing=True)
    yf = model.predict(Xf)

    plt.scatter(t, y, label='y', color='black', zorder=2)
    plt.plot(tf, yf, label='fitted values', color='purple', zorder=1)
    plt.xlabel('t'); plt.ylabel('y'); plt.legend(); plt.show()

if __name__== "__main__":
    n = 10 # Because this fits up to t^(n-1), it seems to break above 10 due to large numbers
    print(perfect_fit(n))