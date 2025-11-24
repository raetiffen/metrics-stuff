# metrics-stuff

OLS:
* [OLS algorithm using modified Gram-Schmidt](</OLS algorithms/modified gram schmidt.py>)
* [OLS algorithm using recursive FWL decompositions](</OLS algorithms/recursive fwl.py>)
* [OLS algorithm which inverts X'X directly by recursively applying the block matrix inverse formula](</OLS algorithms/recursive block inverse.py>)

Ridge:
* [Ridge regression algorithm which appends lambda*I to the bottom of X and solves with modified Gram-Schmidt](</Ridge algorithms/ridge mgs.py>)
* [Ridge regression algorithm which regresses X'y on (X'X + lambda*I) using modified Gram-Schmidt](</Ridge algorithms/ridge mgs alt.py>)
* [Ridge regression algorithm which inverts (X'X + lambda*I) directly by recursively applying the block matrix inverse formula](</Ridge algorithms/ridge recursive block inverse.py>)

Misc:
* [A cool curve generator that fits successive powers of t to normally-distributed data](<Misc/perfect fit.py>)
* [A comparison of the recursive block inverse algorithm with numpy's linalg.inv function](</Misc/testing block inverse.py>)