
## Sheet 3



Exercises with a star on the side must be done
before coming to the class.  Exercises with a hat on the side will be
tackled in class. The others are left as self-exercise.


### Task 1*

Consider the training data $D=\{(x_i,y_i)\}$ for $i=1..m$ where the
$x_i$ are the values of a regressor variable and $y_i$ are the values of
a corresponding response. For example, consider the following data:

$$
D=\{(5, 110),
	(7, 114),
	(9, 118),
	(4, 108)\} 
$$ 

Write the $A$ matrix that appears in the normal equations to estimate
the least square solution of the linear regression for the model
$y=b_0+b_1x+b_2x^2$.

Next, consider a case with two regressor variables $x_1$ and $x_2$ and
one response variable $y$ and a set of training data:
$D=\{(x_{i1},x_{i2},y_i)\}=\{(\mathbf{x}_{i},y_i)\}$. For example, let
it be:

$$
D=\{(1, 1, 6),
    (6, 5, 8),
	(7, 6, 9),
    (7, 7, 12)\}
$$

Write the $A$ matrix that appears in the normal equations to
estimate the least square solution for the model
$y=b_0+b_1x_1+b_2x_2+b_3x_1x_2$.

[The data in the examples are random data generated with:
```
X = np.random.randint(0,10,(4,1))
Y = np.apply_along_axis(lambda x: 100+2*x[0], 1, X)
D = np.column_stack([X,Y])

X = np.random.randint(0,10,(4,2))
Y = np.apply_along_axis(lambda x: 5-2*x[0]+3*x[1], 1, X)
D = np.column_stack([X,Y])
```
]

### Task 2*

Write a function that accepts an $m \times n$ matrix $A$ of rank $n$ and
a vector $\mathbf{b}$ of length $n$.  Use the QR decomposition
<!--
\[
\begin{array}{cccc}
\nonumber
A^{\mathsf T} A\widehat{\mathbf{x}} &= A^{\mathsf T} \mathbf{b} \\ \nonumber
(Q R)^{\mathsf T} Q R  \widehat{\mathbf{x}}
&= (Q R)^{\mathsf T} \mathbf{b} \\ \nonumber
 R^{\mathsf T} Q^{\mathsf T} Q R  \widehat{\mathbf{x}}
&=  R^{\mathsf T} Q^{\mathsf T} \mathbf{b} \\ \nonumber
 R^{\mathsf T} R \widehat{\mathbf{x}}
&=  R^{\mathsf T} Q^{\mathsf T} \mathbf{b} \\
 R \widehat{\mathbf{x}}
&= Q^{\mathsf T} \mathbf{b}
\end{array}
\]
-->
to solve the normal equations corresponding to $A\mathbf{x} =
\mathbf{b}$.

You may use either SciPy's QR routine or write your own QR routine.
In addition, you may use `la.solve_triangular()`, SciPy's optimized
routine for solving triangular systems. Compare the results of your
function with the hand-computed results on the small example generated
by the data set $\\{(0,1),(2,1),(2,2)\\}$: 

$$ 
A=\begin{bmatrix}
0&1\\
2&1\\
2&1
\end{bmatrix}
\qquad b=\begin{bmatrix}
1\\
1\\
2
\end{bmatrix}
$$


### Task 3^

Solve the normal equations from the previous Task by an iterative
method. Compare the numerical results with those from the previous
Task. Compare the execution time of the iterative method against the QR
decomposition from the previous Task (for example using the facilities
from the `benchmark.py` script).

### Task 4*


We have learned that for solving a system of linear equations
$A\mathbf{x}=b$ with $A$ square and invertible the following methods are
available:

1. Gaussian-Jordan elimination
2. Matrix inverse
3. QR decomposition
4. LU decomposition (only for square matrices)
5. Numerical methods (aka iterative methods)



Analyze the computational complexity of the first three methods and in
particular of the Gram-Schmidt orthogonalization, which is the
bottleneck of method 3.



### Task 5^


The file [`housing.npy`]({{ "/assets/housing.npy" | absolute_url }})
(Numpy provides methods for saving and loading arrays. This file has
been saved with `np.save()` and the array can be loaded with
`np.load("housing.npy")`) contains the purchase-only housing price
index, a measure of how housing prices are changing, for the
[United States](http://www.fhfa.gov/DataTools/Downloads/Pages/House-Price-Index.aspx)
from 2000 to 2010. Each row in the array is a separate measurement; the
columns are the year and the price index, in that order.  To avoid large
numerical computations, the year measurements start at 0 instead of
2000.

Find the least squares line that relates the year to the housing price
index (i.e., let year be the $x$-axis and index the $y$-axis).


- Construct the matrix $A$ and the vector $\mathbf{b}$ described in the
    slides. (Hint: `np.vstack()`, `np.column_stack()`, and/or
    `np.ones()` may be helpful.)
- Use your function from the previous task to find the least squares solution.
- Plot the data points as a scatter plot.
- Plot the least squares line with the scatter plot.




### Task 6^


The data in [`housing.npy`]({{ "/assets/housing.npy" | absolute_url }}) is nonlinear, and might be better fit by a
polynomial than a line.

Write a function that uses the procedure presented in the slides to
calculate the polynomials of degree $3$, $6$, $9$, and $12$ that best
fit the data.  Plot the original data points and each least squares
polynomial together in individual subplots. (Hint: for plotting, define
a separate, refined domain with `np.linspace()` and use this domain to
smoothly plot the polynomials.)

Instead of using the procedure developed in Task 1 to solve the normal
equations, you may use SciPy's least squares routine,
`scipy.linalg.lstsq()`.

```Python
>>> from scipy import linalg as la

# Define A and b appropriately. Get help with the `np.vander` function
# for the construction of A

# Solve the normal equations using SciPy's least squares routine.
# The least squares solution is the first of four return values.
>>> x = la.lstsq(A, b)[0]
```

Compare your results to `np.polyfit()`.  This function receives an
array of $x$ values, an array of $y$ values, and an integer for the
polynomial degree, and returns the coefficients of the best fit
polynomial of that degree.

<!--
\begin{comment}
\begin{lstlisting}
# Generate some random data close to the line y = x^2 - 3x + 2.
>>> x = np.linspace(0, 10, 20)
>>> y = x**2 - 3*x + 2 + np.random.randn(20)

# Use np.polyfit() to calculate the best fit 2nd degree polynomial.
>>> coeffs = np.polyfit(x, y, 2)

>>> domain = np.linspace(0, 10, 200)
>>> plt.plot(x, y, 'k*')
>>> plt.plot(domain, np.polyval(coeffs, domain))
>>> plt.show()
\end{lstlisting}
-->



### Task 7^

Consider a case of multiple regression, that is, a prediction task with
more than one predictor. Construct a set of training data randomly
generated with Numpy functions to create matrices. Use two input
variables $x_1$ and $x_2$ and one output variable $y$. 

For example, you can take $x_1\in [0,1]$ $x_2\in [0,1]$ and compute the
corresponding $y$ values with an unknown target function: 

$$
y = x_1^2-7x_1+2x_2^2+5x_2+\epsilon
$$

where $\epsilon$ is an exponentially distributed noise with mean 1.

Fit the model

$$
y=a_2x_2+a_1x_1+a_0
$$

using the routines developed in the previous tasks, preferably the ones
from Task 1, alternatively `scipy.linalg.lstsq()`.

Use the model found to calculate the training error, that is the sum of
squared errors (or the root of it) on the same set of data used for the
estimation of the model coefficients.

Plot the points and the surface of the fitted model in a 3D plot.


Repeat the operations above with the model 

$$
y=a_4x_1^2+a_3x_1+a_2x_2^2+a_1x_2+a_0
$$

Which of the two models is the best?



### Task 8 

For this task you need to study the slides on "Fitting a circle".

The general equation for an ellipse is

$$ax^2 + bx + cxy + dy + ey^2 = 1.$$

Write a function that calculates
the parameters for the ellipse that best fits the data in the file
[`ellipse.npy`]({{ "/assets/ellipse.npy" | absolute_url }}).  Plot the
original data points and the ellipse together, using the following
function to plot the ellipse.

```Python
def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)
    plt.plot(r*cos_t, r*sin_t, lw=2)
    plt.gca().set_aspect("equal", "datalim")
```


