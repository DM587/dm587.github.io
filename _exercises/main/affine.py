# %%
from fractions import Fraction
import numpy as np
np.set_printoptions(precision=3, suppress=True)

# %%
def affine_scaling(c, A, b, x_0, alpha=0.5):
    x = x_0
    x_old=np.zeros(len(x))

    while np.linalg.norm(x_old-x)>0.001:
        x_old=x
        D=np.diag(x)
        D1=np.linalg.inv(D)
        
        x_tilde = D1 @ x
        A_tilde = A @ D
        c_tilde = c @ D
        
        P=np.identity(len(x))-A_tilde.T @ np.linalg.inv( A_tilde @ A_tilde.T) @ A_tilde
        p_tilde=P@c_tilde
        
        mu = np.max([abs(v) for v in p_tilde if v<0])
        
        x_tilde = x_tilde+alpha/mu*p_tilde
        x = D @ x_tilde
        print(x)
    return x

# %%
c = np.array([1, 2, 0])
A = np.array([[1, 1, 1]])
b = np.array([8])

x_0=np.array([1,3,4])
alpha = 0.5

affine_scaling(c, A, b, x_0, alpha)

# %%

c = np.array([2, 3, 2])
A = np.array([[1, 1, 2]])
b = np.array([3])

x_0=np.array([1, 3/2, 1/4])
alpha = 0.5

affine_scaling(c, A, b, x_0, alpha)

# %%

c = np.array([5, 4, 3, 0, 0, 0])
A = np.array([[2, 3, 1, 1, 0, 0],
            [4, 1, 2, 0, 1, 0],
            [3, 4, 2, 0, 0, 1],
            ])
b = np.array([5, 11, 8])

x_0=np.array([0.5, 1, 0.5, 0.5, 7, 1.5])
alpha = 0.5

affine_scaling(c, A, b, x_0, alpha)
