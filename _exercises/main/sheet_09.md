---
layout: default
mathjax: true
title:  Sheet 9 
date:   2021-12-14 08:33:19 +0100
categories: exercises 
---

## Sheet 9


### Task 1

Model mathematically an input/output open economy with three
commodities. Then, using the numerical values for $a_{ij}$ and $d_i$
determined by the python code below, find the amounts to be produced
for each of the three commodities in order to satisfy all demands
exactly.


```
#!/usr/bin/python
import numpy as np

np.random.seed(0000000001)
np.set_printoptions(precision=3)

def generate_data():
   '''
   return the matrix A
   Example:
   >>> A = generate_data()
   '''
   np.set_printoptions(precision=3)
   for i in range(1000):
       A=np.random.rand(3,3)
       s=np.sum(A,axis=1)
       if (s<1).all(): break
   return A

d = np.random.randint(10000,100000,3)
A = generate_data()

print(A)
print(d)
```



### Task 2

The numerical data for the cases discussed in class are collected in
this
[spreadsheet](https://docs.google.com/spreadsheets/d/1yWCM0e-qjshjL0IHv8KbbM2csX-Lvi-Wl3nM707f6ac/edit?usp=sharing).


Model these cases mathematically again and solve them numerically using
Spreadsheets tools and Python as follows.

#### Mathematical optimization in spreadsheets:

Recall that, in a spreadsheet we can carry out summations:

$$
\sum_{j=1}^nc_j=c_1+c_2+\ldots+c_n
$$

with $\mathtt{SUM(B5:B14)}$
and scalar products

$$
\begin{array}{ll}
\vec u\cdot\vec v &= u_1v_1+u_2v_2+\ldots + u_nv_n\\
&=\sum\limits_{j=1}^nu_jv_j
\end{array}
$$

with $\mathtt{SUMPRODUCT(B5:B14,C5:C:14)}$.

Instructions on add-ons for Excel:

- [Microsoft Office Excel add-on](https://support.office.com/en-gb/article/Load-the-Solver-Add-in-in-Excel-612926fc-d53b-46b4-872c-e24772f078ca?ui=en-US&rs=en-GB&ad=GB)
- [OpenSolver](https://opensolver.org/)


Instruction on add-ons for Google Sheets:


- [FrontlineSolvers](https://www.solver.com/)
- [OpenSolver](https://opensolver.org/opensolver-for-google-sheets/)
- [Google Optimization Tools](https://developers.google.com/optimization/lp/add-on)


#### Mathematical optimization in Python 

Find the `linprog` function from the submodule dedicated to
[optimization](https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html)
in the `scipy` module and follow the instructions there. You can read
the data from a spreadsheet using, for example, the module `pandas` or
`openpyxl` or read this
[post](https://towardsdatascience.com/read-excel-files-with-python-1000x-faster-407d07ad0ed8).


### Task 3: Knapsack Problem

Model in linear programming terms the following problem: Given a set of
items, each with a weight and a value, determine the number of each item
to include in a collection so that the total weight is less than or
equal to a given limit and the total value is as large as possible.
Reason about the nature of the variables, continuous or discrete, and
solve the following instance of the problem:

```{python}
import numpy as np

num_items=100
capacity=997
values = np.array([585, 194, 426, 606, 348, 516, 521, 1092, 422, 749, 895, 337, 143, 557, 945, 915, 1055, 546, 352, 522, 109, 891, 1001, 459, 222, 767, 194, 698, 838, 107, 674, 644, 815, 434, 982, 866, 467, 1094, 1084, 993, 399, 733, 533, 231, 782, 528, 172, 800, 974, 717, 238, 974, 956, 820, 245, 519, 1095, 894, 629, 296, 299, 1097, 377, 216, 197, 1008, 819, 639, 342, 807, 207, 669, 222, 637, 170, 1031, 198, 826, 700, 587, 745, 872, 367, 613, 1072, 181, 995, 1043, 313, 158, 848, 403, 587, 864, 1023, 636, 129, 824, 774, 889])
weights = np.array([485, 94, 326, 506, 248, 416, 421, 992, 322, 649, 795, 237, 43, 457, 845, 815, 955, 446, 252, 422, 9, 791, 901, 359, 122, 667, 94, 598, 738, 7, 574, 544, 715, 334, 882, 766, 367, 994, 984, 893, 299, 633, 433, 131, 682, 428, 72, 700, 874, 617, 138, 874, 856, 720, 145, 419, 995, 794, 529, 196, 199, 997, 277, 116, 97, 908, 719, 539, 242, 707, 107, 569, 122, 537, 70, 931, 98, 726, 600, 487, 645, 772, 267, 513, 972, 81, 895, 943, 213, 58, 748, 303, 487, 764, 923, 536, 29, 724, 674, 789])
```

In Python with `scipy.optimization.linprog` you can only solve for
continuous variables with one of the latest versions of scipy. It is
anyway a good exercise to solve the problem with continuous variables
and then try to derive an integer solution from the fractional one. How
would you do? Compare your results with the optimal integer solution for
this instance has objective function value: 2397.



<!--
### Task 3 - Quizzies

Basic Geometric Facts:

-   In 4D, how many hyperplanes need to intersect to give a point?

-   In 4D, can a point be described by more than 4 hyperplanes?

-   Consider the intersection of $n$ hyperplanes in $n$ dimensions: when
    does it uniquely identify a point?

Vertices of Polyhedra:

Consider the polyhedron described by
$A{\mathbf{x}}\leq {\mathbf{b}}$, $A\in
{\mathbb{R}}^{m\times n}, {\mathbf{x}} \in {\mathbb{R}}^n$,
that is: 

$$\begin{array}{*{10}{c}}
a_{11}x_1&+&a_{12}x_2&+&\cdots&+&a_{1n}x_n&\leq&b_1\\
a_{21}x_1&+&a_{22}x_2&+&\cdots&+&a_{2n}x_n&\leq&b_2\\
&&\vdots&&&&&\vdots&\\
a_{m1}x_1&+&a_{m2}x_2&+&\cdots&+&a_{mn}x_n&\leq&b_m\\
\end{array}$$


-   How many constraints are *active* in a *vertex* of a polyhedron
    $A{\mathbf{x}}\leq {\mathbf{b}}$,
    $A\in {\mathbb{R}}^{m\times n}, {\mathbf{x}} \in {\mathbb{R}}^n$?

-   Does every point $x$ that activates $n$ constraints form a vertex of
    the polyhedron?

-   Can a vertex activate more than $n$ constraints?


-   What if there are more variables than constraints? If $n>m$ then
    we can find a subset of them and then activate constraints. But
    what if we have more constraints than variables, ie, $m>n$, can we
    have a vertex?

-   Combinatorial explosion of vertices: how many constraints and
    vertices has an $n$-dimensional hypercube?

-   If there are $m$ constraints and $n$ variables, $m>n$, what is an
    upper bound to the number of vertices?

Basic Solutions and Vertices

-   For each of these three statements, say if they are true or false:

    -   One basic solution $\Longrightarrow$ one vertex of the feasible region

    -   One basic solution $\Longleftarrow$ one vertex of the feasible region

    -   One basic solution $\Longleftrightarrow$ one vertex of the feasible
        region

-   Consider the following LP problem:

    $$\begin{array}{*{6}{c}}
    \max & 6x_1&+&8x_2\\
    &5x_1&+&10x_2&\leq&60\\
    &4x_1&+&4x_2&\leq&40\\
    &x_1, &x_2 &\geq& 0\\
    \end{array}$$

    -   How many variables (original and slack) can be different from
        zero in a solution?

    Let's generalize the previous case. Consider an LP with $m$
    constraints, $n$ original variables and $m$ slack variables. In an
    optimal solution:

    -   is $m>n$, how many variables (original and slack) can be nonzero
        at most?

    -   If $m<n$ how many original variables must be zero at least? In
        other terms, in a mix planning problem with $n$ products and
        $m$, $m<n$ resources, how many products at most will be to be
        produced in an optimal solution?



-   If in the original space of the problem we had 3 variables, and
    there are 6 constraints, how many constraints would be active in
    an optimal solution?


-   For the general case with $n$ original variables:\
    One basic feasible solution $\Longleftrightarrow$ a matrix of active
    constraints has rank $n$. True or False?


-   Consider an LP problem with $m$ constraints and $n$ original
    variables, $m>n$. We saw that in $\mathbb{R}^n$ a point is the
    intersection of at least $n$ hyperplanes. In LP this corresponds
    to say that in a vertex there are $n$ active constraints. Let a
    basic solution be associated with a solution that makes exactly
    $n+1$ constraints active, what can we say about the corresponding
    basic and non-basic variable values?

-   What is the algebraic definition of adjacency between two vertices
    of a polyhedron in $2$, $3$ and $n$ dimensions?

-   How does this condition translate on basic variables of the two basic solutions?
-->
