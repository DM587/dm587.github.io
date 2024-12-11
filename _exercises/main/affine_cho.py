
# %%
import numpy as np
import scipy as sp
import scipy.linalg as spla

np.set_printoptions(precision=3, suppress=True)


# %%
A = np.array([
    [3,2,-4],
    [2, 0, 7],
    [-4, 7,4]    
    ])

AA = A @ A.T

print(AA)

L=spla.cholesky(AA, lower=True)

print(L)
print(np.allclose(AA, L @ L.T))

print(spla.cho_factor(AA))

# %%

def affine_scaling_cho(c, A, b, x_0, alpha=0.5):
    x = x_0
    x_old=np.zeros(len(x))

    while np.linalg.norm(x_old-x, ord=2)>0.001:
        x_old=x
        D=np.diag(x)
        D1=np.linalg.inv(D)
        
        x_tilde = D1 @ x
        A_tilde = A @ D
        c_tilde = c @ D
                
        v=A_tilde @ c_tilde
        AA = A_tilde @ A_tilde.T

        if True:
            ## solve AA^T w = v
            L = spla.cholesky(AA, lower=True)
            ## LL^T w = v 
            ## Ly=v
            ## L^Tw=y
            y = spla.solve_triangular(L, v, lower = True)
            w = spla.solve_triangular(L.T, y, lower = False)
        else:
            L, low = spla.cho_factor(AA)
            w = spla.cho_solve((L, low), v)
        
        p_tilde = c_tilde - A_tilde.T @ w
        
        theta = np.max([abs(v) for v in p_tilde if v<0])
        
        x_tilde = x_tilde + alpha/theta * p_tilde
        x = D @ x_tilde
        print(x)
    return x

# %%

c = np.array([5, 4, 3, 0, 0, 0])
A = np.array([[2, 3, 1, 1, 0, 0],
            [4, 1, 2, 0, 1, 0],
            [3, 4, 2, 0, 0, 1],
            ])
b = np.array([5, 11, 8])

x_0=np.array([0.5, 1, 0.5, 0.5, 7, 1.5])
alpha = 0.5

affine_scaling_cho(c, A, b, x_0, alpha)
# %%


