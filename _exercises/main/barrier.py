# %% 

import numpy as np
import scipy as sp


# %%


def barrier(A, b, c) -> int:
    """
    max 5x1 + 4x2 + 3x3                   max 5y1 + 11y2 + 8y3
    s.t. 2x1 + 3x2 + x3 + w1 = 5          s.t. 2y1 + 4y2 + 3y3 + z1 ≤ 5
        4x1 + x2 + 2x3 + w2 = 11              3y1 + y2 + 4y3 + z2 ≤ 4
        3x1 + 4x2 + 2x3 + w3 = 8              y1 + 2y2 + 2y3 + z3 ≤ 3
        x1 , x2 , x3 , w1 , w2 , w3 ≥ 0       y1 , y2 , y3 , z1 , z2 , z3 ≥ 0
    """

    x = np.array(len)
    w
    y
    z



c = np.array([5,4,3])
A = np.array([[2,3,1],
            [4,1,2],
            [3,4,2]])
b = np.array([5,11,8])

# %%

n = 
m =
cq = np.vstack()
Aq = 
