
## Task 1: Linear Programming by Affine Scaling 

Implement in python the affine-scaling method and solve the following problem:

$$
\begin{array}{rl}
  \max\;& z=x_1+2x_2\\
  &x_1+x_2\leq 8\\
  &x_1\geq 0,x_2\geq 0 
\end{array}
$$

It is the same problem as seen in the slides. But now solve it assuming the starting solution is $[x_1, x_2]=[1, 3]$. The optimal solution is $[0,8]$.

You can then solve also the following problem:

$$
\begin{array}{rl}
\text{maximize} \;\;&2x_1 + 3x_2 + 2x_3 \\
\text{subject to} \; \; &x_1 + x_2 +2x_3 = 3\\
&x_1,x_2,x_3 \geq 0.
\end{array}
$$

using as starting solution $[x_1, x_2, x_3]=[1, 3/2, 1/4]$.

How should the algorithm change if the problem was a minimization problem?

{% if page.solution %}
<font color="blue">
Solution:

{% highlight python %}
{% include_relative main/affine.py %}
{% endhighlight %}

{% highlight python %}
[1.046 4.954 2.   ]
[0.934 6.066 1.   ]
[0.724 6.776 0.5  ]
[0.465 7.285 0.25 ]
[0.249 7.626 0.125]
[0.125 7.812 0.062]
[0.063 7.906 0.031]
[0.031 7.953 0.016]
[0.016 7.977 0.008]
[0.008 7.988 0.004]
[0.004 7.994 0.002]
[0.002 7.997 0.001]
[0.001 7.999 0.   ]
[0.    7.999 0.   ]

[0.636 2.114 0.125]
[0.318 2.536 0.073]
[0.159 2.763 0.039]
[0.08  2.881 0.02 ]
[0.04 2.94 0.01]
[0.02  2.97  0.005]
[0.01  2.985 0.002]
[0.005 2.993 0.001]
[0.002 2.996 0.001]
[0.001 2.998 0.   ]
[0.001 2.999 0.   ]
[0. 3. 0.]
{% endhighlight %}

</font>
{% endif %}


## Task 2: Linear Programming for Project Selection

Model in linear programming terms the following problem: Given a set of
projects to invest on, each with a cost and an expected profit, determine which
to include in a collection so that the total cost is less than or
equal to a given budget and the total expected profit is as large as possible.
Reason about the nature of the variables, continuous or discrete.

Solve the instance of the problem given in the python code below in two ways:

- with `scipy.optimization.linprog` from the latest versions of scipy,

- with your implementation of the Affine Scaling method seen in the lecture.


The previous solution methods will only solve the continuous variables case. It is
anyway a good exercise to solve the problem with continuous variables
and then try to derive an integer solution from the fractional one. How
would you do? 

<!--
Compare your results with the optimal integer solution for
this instance has objective function value: 2397.
-->



```{python}
import numpy as np

num_items=100
capacity=997
profit = np.array([585, 194, 426, 606, 348, 516, 521, 1092, 422, 749, 895, 337, 143, 557, 945, 915, 1055, 546, 352, 522, 109, 891, 1001, 459, 222, 767, 194, 698, 838, 107, 674, 644, 815, 434, 982, 866, 467, 1094, 1084, 993, 399, 733, 533, 231, 782, 528, 172, 800, 974, 717, 238, 974, 956, 820, 245, 519, 1095, 894, 629, 296, 299, 1097, 377, 216, 197, 1008, 819, 639, 342, 807, 207, 669, 222, 637, 170, 1031, 198, 826, 700, 587, 745, 872, 367, 613, 1072, 181, 995, 1043, 313, 158, 848, 403, 587, 864, 1023, 636, 129, 824, 774, 889])
cost = np.array([485, 94, 326, 506, 248, 416, 421, 992, 322, 649, 795, 237, 43, 457, 845, 815, 955, 446, 252, 422, 9, 791, 901, 359, 122, 667, 94, 598, 738, 7, 574, 544, 715, 334, 882, 766, 367, 994, 984, 893, 299, 633, 433, 131, 682, 428, 72, 700, 874, 617, 138, 874, 856, 720, 145, 419, 995, 794, 529, 196, 199, 997, 277, 116, 97, 908, 719, 539, 242, 707, 107, 569, 122, 537, 70, 931, 98, 726, 600, 487, 645, 772, 267, 513, 972, 81, 895, 943, 213, 58, 748, 303, 487, 764, 923, 536, 29, 724, 674, 789])
```


{% if page.solution %}
<font color="blue">

Solution:

Let $\vec p$ be a vector of profits of the project, $a$ a vector of costs of the projects and $\vec 0 \leq \vec x\leq \vec 1$ be a vector of decision variables saying how much we want to invest for each project.

Then the model of the problem is:

$$
\begin{array}{rl}
\max\; & \vec p^T \vec x\\
&\vec a^T \vec x \leq \vec b\\
&\vec x\leq \vec 1\\
&\vec x \geq \vec 0
\end{array}
$$

Implementation:

{% highlight python %}
{% include_relative main/knapsack.py %}
{% endhighlight %}

{% highlight python %}
15239.857191091372
{% endhighlight %}

</font>
{% endif %}


## Task 3

Show that if $A$ is a square matrix that can be reduced to a row echelon form $U$ by
Gaussian elimination without row interchanges, then $A$ can be factored
as $A = LU$, where $L$ is a lower triangular matrix.

Show that the LU decomposition can be rewritten as 

$$
    A=LDU
$$

where now both the lower
triangular factor and the upper triangular factor have 1's on the main diagonal.


{% if page.solution %}<!-- ------------------------------------------ -->
<font color="blue">
Solution:

We know that the Gaussian elimination operations can be accomplished
by multiplying $A$ on the left by an appropriate sequence of elementary
matrices; that is, there exist elementary matrices $E_1,E_2,...,E_k$
such that

$$
E_k \cdots E_2E_1A = U'
$$

where U' is an upper triangular matrix with entries equal to 1 in the diagonal.

Since elementary matrices are invertible, we can solve for $A$ as

$$
A = E_1^{-1}E_2^{-1} \cdots E_k^{-1}U
$$

$$
A = LU'
$$

$$
L = E_1^{-1}E_2^{-1} \cdots E_k^{-1}
$$

$L$ is lower triangular because:

- multiplying a row by a nonzero constant, and adding a scalar multiple of one row to another generate elementary matrices that are lower triangular.
  
- multiplication of lower traingular matrices preserves the lower triangular property

- inverse of lower traingular matrices preserves the lower triangular property.

<br>
To show that the $LU'$ decomposition can be rewritten as 
$$
    A=L'DU'
$$
we just ``shift'' the diagonal entries of $L$ to a diagonal matrix $D$ and write $L$ as $L' =
LD'$.


In general, $LU$-decompositions are not unique.

$$
A=LU=
\begin{bmatrix}
  l_{11}& 0 &0 \\
  l_{21}& l_{22}& 0 \\
  l_{31}& l_{32}& l_{33}\\
\end{bmatrix}
\begin{bmatrix}
1 &u_{12} &u_{13}\\
0 &1 &u_{23}\\
0 &0 &1\\
\end{bmatrix}
$$

and $L$ has nonzero diagonal entries (which will be true if $A$ is invertible), then we can
shift the diagonal entries from the left factor to the right factor by writing

$$
\begin{array}{rl}
A=&
\begin{bmatrix}
  1 &0&0\\
  l_{21}/l_{11}& 1& 0\\
  l_{31}/l_{11} &l_{32}/l_{22}& 1
\end{bmatrix}
\begin{bmatrix}
  l_{11}&0&0\\
  0& l_{22} &0 \\
   0 &0& l_{33} 
\end{bmatrix}
\begin{bmatrix}
  1&u_{12}&u_{13}\\
  0& 1 &u_{23}\\
  0 &0 &1 
\end{bmatrix}
\\
= &
\begin{bmatrix}
  1& 0& 0\\
  l_{21}/l_{11}& 1 &0\\
  l_{31}/l_{11}& l_{32}/l_{22}&1\\ 
\end{bmatrix}
\begin{bmatrix}
  l_{11} &l_{11}u_{12}& l_{11}u_{13}\\
   0& l_{22}& l_{22}u_{23}\\
  0 &0 &l_{33}\\
\end{bmatrix}
\end{array}
$$

which is another LU-decomposition of $A$.

</font>
{% endif %}


## Task 4

Propose and efficient method for solving $Ax=b$ and $A^T\tilde{x}=\tilde{b}$.


## Task 5

Find the LU decomposition of the matrix 

$$
A=\begin{bmatrix}
3 &−6 &−3 \\
2 &0 &6 \\
−4 &7 &4 
\end{bmatrix}.
$$

Using the decomposition:

- solve the system of linear equations: $Ax=b$ when $b=[-3, -22, 3]$
- find the inverse of $A$.



## Task 6

Software libraries vary in how they handle LU-decompositions. For example, many libraries perform row interchanges to reduce roundoff error and hence produce PLU-decompositions, even when asked for LU-decompositions. Find out which function(s) performs the LU-decomposition in Python Scipy and see what happens when you use scipy to find an LU-decomposition of the matrix from the previous task. (Hint: compare `scipy.linalg.lu`, `scipy.linalg.lu_factor`, `scipy.linalg.lu_solve`, `scipy.sparse.linalg.splu`). Update your implementation of Task 1 such that it does not need to compute any matrix inversion.

## Task 7: Modeling

The figure below shows a metal plate whose edges are held at the temperatures shown. It follows from thermodynamic principles that the temperature at each of the six interior nodes will eventually stabilize at a value that is approximately the average of the temperatures at the four neighboring nodes. These are called the steady-state temperatures at the nodes. 

<!-- Thus, for example, if we denote the steady-state temperatures at the interior nodes in the figure as $T_1, T_2, T_3, T_4, T_5$, and $T_6$, then at the node labeled $T_1$ that temperature will be T1 = 41 (0 + 5 + T2 + T3) or, equivalently,
4T1 − T2 − T3 = 5
-->
Find a linear system whose solution gives the steady-state temperatures at the nodes, and use scipy to solve that system by LU-decomposition.

<img src="./figures/temperature.png" alt="points1" style="width:400px;"/>




{% if page.solution %}<!-- ------------------------------------------ -->
<font color="blue">
Solution:

At node $T_i$ the temperature will be:
$$
T_{i,j}=\frac{1}{4}(T_{i-1,j}+T_{i+1,j}+T_{i,j-1},T_{i,j+1})
$$
so:

$$
\begin{array}{rl}
T_1=&\frac{1}{4}(0+5+T_2+T_3)\\
T_2=&\frac{1}{4}(0+20+T_1+T_4)\\
T_3=&\frac{1}{4}(5+T_1+T_5+T_4)\\
T_4=&\frac{1}{4}(20+T_2+T_3+T_6)\\
T_5=&\frac{1}{4}(5+10+T_3+T_6)\\
T_6=&\frac{1}{4}(10+20+T_5+T_4)
\end{array}
\qquad 

$$
\begin{array}{rl}
&4T_1-T_2-T_3=5\\
&4T_2-T_1-T_4=20\\
&4T_3-T_1-T_5-T_4=5\\
&4T_4-T_2-T_3-T_6=20\\
&4T_5-T_3-T_6=15\\
&4T_6-T_5-T_4=30
\end{array}
$$
$$

</font>
{% endif %}