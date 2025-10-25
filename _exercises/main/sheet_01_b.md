
### Task 1^  -  Handling Exceptions

A *random walk* is a path created by a sequence of random steps. The
following function simulates a random walk by repeatedly adding or
subtracting $1$ to a running total.

    from random import choice

    def random_walk(max_iters=1e12):
        walk = 0
        directions = [1, -1]
        for i in range(int(max_iters)):
            walk += choice(directions)
        return walk

A <span>`KeyboardInterrupt`</span> is a special exception that can be
triggered at any time by entering <span>`ctrl+c`</span> (on most
systems) in the keyboard. Modify <span>`random_walk()`</span> so that if
the user raises a <span>`KeyboardInterrupt`</span> by pressing
<span>`ctrl+c`</span> while the program is running, the function catches
the exception and prints “Process interrupted at iteration $i$”. If no
<span>`KeyboardInterrupt`</span> is raised, print “Process completed”.
In both cases, return <span>`walk`</span> as before.

### Task 2^  -  File Input/Output

Define a class called <span>`ContentFilter`</span>. Implement the
constructor so that it accepts the name of a file to be read.

1.  If the file name is invalid in any way, prompt the user for another
    filename using <span>`input()`</span>. Continue prompting the user
    until they provide a valid filename.

        >>> cf1 = ContentFilter("hello_world.txt")  # File exists.
        >>> cf2 = ContentFilter("not-a-file.txt")   # File doesn't exist.
        <<Please enter a valid file name: >><r<still-not-a-file.txt>r>
        <<Please enter a valid file name: >><r<hello_world.txt>r>
        >>> cf3 = ContentFilter([1, 2, 3])          # Not even a string.
        <<Please enter a valid file name: >><r<hello_world.txt>r>

    (Hint: <span>`open()`</span> might raise a
    <span>`FileNotFoundError`</span>, a <span>`TypeError`</span>, or an
    <span>`OSError`</span>.)

2.  Read the file and store its name and contents as attributes (store
    the contents as a single string). Make sure the file is
    securely closed.

### Task 3^  -  Matrix Multiplication in Numpy

Matrix Multiplication in Numpy There are two main ways to perform matrix
multiplication in NumPy: with NumPy’s <span>`dot()`</span> function
(<span>`np.dot(A, B)`</span>), or with the <span>`@`</span> operator
(<span>`A @ B`</span>). Write a function that defines the following
matrices as NumPy arrays. 

$$\begin{aligned}
A = \left[\begin{array}{rrr}
3 & -1 &  4 \\
1 &  5 & -9 \end{array}\right]
&&
B = \left[\begin{array}{cccc}
2 &  6 & -5 &  3\\
5 & -8 &  9 &  7\\
9 & -3 & -2 & -3\end{array}\right]\end{aligned}$$ 

Return the matrix product $AB$. For examples of array initialization and
matrix multiplication, use object introspection in IPython to look up
the documentation for <span>`np.ndarray`</span>,
<span>`np.array()`</span> and <span>`np.dot()`</span>.

    In [1]: import numpy as np

    In [2]: np.array?       # press 'enter'

### Task 4^  -  Matrix Multiplication

Write a function that defines the following matrix as a NumPy array.

$$A = \left[\begin{array}{rrr}
3 & 1 & 4\\
1 & 5 & 9 \\
-5 & 3 & 1 \end{array}\right]$$ 

Return the matrix $-A^3 + 9A^2 - 15A$.

In this context, $A^2 = AA$ (the matrix product, not the component-wise
square). The somewhat surprising result is a demonstration of the
Cayley-Hamilton theorem.

### Task 5^  -  Array Creation

Write a function that defines the following matrices as NumPy arrays
using the functions to create arrays in the slides (that is, without
hard writing all the numbers). Calculate the matrix product $ABA$. Change
the data type of the resulting matrix to <span>`np.int64`</span>, then
return it. $$\begin{aligned}
A = \left[\begin{array}{rrrrrrr}
1 & 1 & 1 & 1 & 1 & 1 & 1\\
0 & 1 & 1 & 1 & 1 & 1 & 1\\
0 & 0 & 1 & 1 & 1 & 1 & 1\\
0 & 0 & 0 & 1 & 1 & 1 & 1\\
0 & 0 & 0 & 0 & 1 & 1 & 1\\
0 & 0 & 0 & 0 & 0 & 1 & 1\\
0 & 0 & 0 & 0 & 0 & 0 & 1\end{array}\right]
&&
B = \left[\begin{array}{rrrrrrr}
-1 &  5 &  5 &  5 &  5 &  5 &  5\\
-1 & -1 &  5 &  5 &  5 &  5 &  5\\
-1 & -1 & -1 &  5 &  5 &  5 &  5\\
-1 & -1 & -1 & -1 &  5 &  5 &  5\\
-1 & -1 & -1 & -1 & -1 &  5 &  5\\
-1 & -1 & -1 & -1 & -1 & -1 &  5\\
-1 & -1 & -1 & -1 & -1 & -1 & -1\end{array}\right]\end{aligned}$$

### Task 6^  -  Arrays

Write a function that accepts a single array as input. Make a copy of
the array, then use fancy indexing to set all negative entries of the
copy to $0$. Return the copy.

### Task 7  -  Arrays

Write a function that defines the following matrices as NumPy arrays.

$$\begin{aligned}
A = \left[\begin{array}{rrr}
0 & 2 & 4\\
1 & 3 & 5\end{array}\right]
&&
B = \left[\begin{array}{rrr}
3 & 0 & 0\\
3 & 3 & 0\\
3 & 3 & 3\end{array}\right]
&&
C = \left[\begin{array}{rrr}
-2 & 0 & 0\\
0 & -2 & 0\\
0 & 0 & -2\end{array}\right]\end{aligned}$$ 


Use NumPy’s stacking functions to create and return the block matrix:

$$\begin{aligned}
\left[\begin{array}{ccc} \mathbf{0}& A^T & I\\ A & \mathbf{0}& \mathbf{0}\\ B & \mathbf{0}& C \end{array}\right],\end{aligned}$$

where $I$ is the $3\times 3$ identity matrix and each
$\mathbf{0}$ is a matrix of all zeros of appropriate
size.

A block matrix of this form is used in the interior point method for
linear optimization.

### Task 8^  -  Arrays

A matrix is called *row-stochastic* if its rows each sum to $1$.
Stochastic matrices are fundamentally important for finite discrete
random processes and some machine learning algorithms.

Write a function than accepts a matrix (as a 2-D array). Divide each row
of the matrix by the row sum and return the new row-stochastic matrix.
Use array broadcasting and the <span>`axis`</span> argument instead of a
loop.

(Similarly, a matrix is called *column-stochastic* if its columns each sum to $1$.)


### Task 9  -  Polynomials

Use NumPy’s polynomial objects to approximate the following series.
    
$$\arcsin x = \sum_{n=0}^{\infty} \frac{\left(2 n\right) ! x^{2 n + 1}}{\left(2 n + 1\right)\left(n!\right)^2 4^n}$$ 
	
The series on the right hand side converges for $n\to \infty$ to
$\arcsin x$ if $x$ in $[-1, 1]$. Use your series approximation to
approximate $\pi$. Use the function `np.allclose` to verify that your
approximation is close.
<!--
Hint: think of the powers of $x$ that are not
included in the series as having zero coefficients.
-->



### Task 10 -- Matrix calculus in `numpy` and `scipy`

The modules `numpy` and `scipy` make available another data structure in
Python, the 'array' type. This exercise guides you to the discovery of
how operators are overloaded for the 'array' type module.

Generate in Python two matrices $A$ and $B$ of size $3\times 2$ and
$2\times 4$, respectively, made of integer numbers randomly drawn from
the interval $[1,\ldots,10]$. Calculate the following results, first by
hand and then checking the correctness of your answer in Python numpy:

a)  $A+B, A-B$

b)  $A\cdot B$

c)  $A/B$

\[In IPython and Jupyter it is possible from command line to ask for
completion via tab. This can be used to explore which functions are
available for a given module. Try for example to type

```
import numpy as np
np.
```

followed by a tab. You should see a list of available functions. Among
them there are two submodules that will be useful for us: `random` and
`linalg`. The first implements a function to generate random numbers and
matrices. The second implements functions from linear algebra. It is
possible to get a manual for each function by following the function
with a question mark. For example: `np.random.randint?`.\]

{% if page.solution %}
    A=np.random.randint(1,10,(3,2))
    B=np.random.randint(1,10,(2,4))
    A+B
    A-B
    A*B

All these produce an error because the `+,-` operators, as in linear
algebra perform an element-wise addition and subtraction, which requires
the two matrices to have exactly the same size.

The `*` operator performs also an element-wise multiplication, which
require the two matrices to have exactly the same size. However,
contrary to addition and multiplication, this operation is not defined
element-wise in linear algebra.

The correct way to obtain the matrix product is:

```
np.dot(A,B)
```

The division by a matrix is not defined in linear algebra. In Python it
does an element-wise operations if the matrices have the same size.

{% endif %}

### Task 11 -- Matrix operations

For some aribtrary dimension and some random numbers in the matrices:

a)  Construct an array of zeros

b)  Concatenate an identity matrix to a matrix

c)  Insert a row in between other two

d)  Print the dimensions of an array

e)  Multiply matrices

f)  Print the matrix transpose

g)  Print the rank of a matrix

### Task 12 -- Matrix Inverse

Calculate the inverse of these two matrices:

$${\displaystyle \mathbf {A} ={\begin{bmatrix}-1&{\tfrac {3}{2}}\\1&-1\end{bmatrix}} \qquad
\mathbf {B} ={\begin{bmatrix}-1&{\tfrac {3}{2}}\\{\tfrac {2}{3}}&-1\end{bmatrix}}.}$$

### Task 13 -- Indexing and slices

Construct an array of dimension $3\times 3$ containing the first 9
natural numbers. Remember that indices start at 0.

a)  print the element at (0,0)

b)  print all rows starting from the second

c)  print the second row of the matrix

d)  print a vector filled by the 3rd column of the matrix

e)  print the type of the data contained in the matrix

f)  change the type of the data in the matrix to be a floating point
    number with 64 bits.

g)  print the size of each dimension of the matrix

h)  flatten the matrix using reshape and ravel

i)  copy the flattened version and change a value in the elements of the
    copy. Show the difference in these operations between shallow and
    deep copy.

### Task 14 -- Construction of matrices and vectors

a)  Construct a matrix of size $3\times 4$ containing only zeros. Which
    type of data contains the matrix created?

b)  Repeat the previous task with a matrix of all ones.

c)  Create an identity matrix of size $4\times 4$

d)  Create a diagonal matrix of size $4\times 4$ containing the first
    four natural numbers in the diagonal

e)  Create a matrix of size $3\times 4$ containing random numbers
    between 0 and 1, extremes included.

f)  Create a matrix of size $3\times 4$ containing random integer
    numbers between 1 and 10, extremes included.

g)  Create an array containing the first 5 integer numbers.

h)  Create an array of incremental numbers from 0 to 5 with intervals of
    0.5.

i)  Concatenate two random matrices of size $3\times 4$ first vertically
    and then horizontally.

### Task 15 -- Solving systems of linear equations

Solve by Gaussian elimination the following system of linear equations
$A{\mathbf{x}}={\mathbf{b}}$ where 

$$A=
\begin{bmatrix}
  3 & 1 & 1 & 1 \\
  2 & 4 & 1 & 1 \\
  2 & 1 & 2 & 2 \\
\end{bmatrix}\qquad 
{\mathbf{b}}=\begin{bmatrix} 2\\  2\\  1\end{bmatrix}$$ 

First
carry out the calculations by hand and then try using Python numpy.
Finally, compare your result with the one of `numpy.linalg.solve`.

{% if page.solution %}

```
A=np.array([[3,1,1,1],
  [2, 4, 1, 1],
  [2,1,2,2]])
b=np.array([ 2, 2, 1])

# np.linalg.solve(A,b)
print np.linalg.matrix_rank(A)
AA=np.column_stack([A,b])
AA=column_stack([A,b])
AA[0,:] = f(1,3) * AA[0,:]  # remember indices start from 0
AA[1,:] = -2 * AA[0,:] + AA[1,:]
AA[2,:] = -2 * AA[0,:] + AA[2,:]
printm(AA)
AA[1,:] = f(3,10)* AA[1,:]
AA[2,:] += -f(1,3) * AA[1,:]
printm(AA)
AA[2,:] = f(10,13) * AA[2,:]
printm(AA)
AA[1,:] += -f(1,10) * AA[2,:]
AA[0,:] += -f(1,3) * AA[2,:]
printm(AA)
AA[0,:] += -f(1,3) * AA[1,:]
printm(AA)
```

After elementary row operations the augmented matrix looks like:

```
[1, 0, 0, 0,  9/13]
[0, 1, 0, 0,  3/13]
[0, 0, 1, 1, -4/13]
```

From here we can write directly the solution: 

$$\begin{array}{rl}
x_1&=9/13\\
x_2&=3/13\\
x_3&=-4/13-t\\
x_4&=t
\end{array}$$

which in vector notation is equivalent to

$$\begin{array}{rl}
{\mathbf{x}}=\begin{bmatrix}9/13\\3/13\\-4/13\\0\end{bmatrix}
+t\begin{bmatrix}0\\0\\-1\\1\end{bmatrix}\end{array}$$

Hence the solution subspace is expressed by an affine combination.
{% endif %}

### Task 16 -- 3D Arrys in `numpy`

a)  Create a 3D array of shape $(3, 3, 3)$ filled with random integers
    between 0 and 9.

{% if page.solution %}
        import numpy as np

        array_3d = np.random.randint(0, 10, (3, 3, 3))
        print("3D Array:\n", array_3d)
{% endif %}

b)  Access the element at position $(1, 2, 1)$ in the 3D array.

{% if page.solution %}
        element = array_3d[1, 2, 1]
        print("Element at position (1, 2, 1):", element)
{% endif %}

c)  Extract a 2D slice from the 3D array. Slice the first matrix (i.e.,
    the 0th index along the first axis).

{% if page.solution %}
        slice_2d = array_3d[0, :, :]
        print("2D Slice from the 3D array (0th matrix):\n", slice_2d)
{% endif %}

d)  Set all elements in the second matrix (i.e., the 1st index along the
    first axis) to 5.

{% if page.solution %}
        array_3d[1, :, :] = 5
        print("3D Array after modification:\n", array_3d)
{% endif %}

e)  Calculate the sum of the elements along axis 0 (collapsing the first
    dimension).

{% if page.solution %}
        sum_axis_0 = np.sum(array_3d, axis=0)
        print("Sum along axis 0:\n", sum_axis_0)
{% endif %}

f)  Reshape the 3D array into a 2D array of shape (9, 3).

{% if page.solution %}
        reshaped_array = array_3d.reshape(9, 3)
        print("Reshaped 2D Array (9, 3):\n", reshaped_array)
{% endif %}

g)  Create a 3D identity matrix of shape (3, 3, 3) where each matrix
    along the first axis is an identity matrix.

{% if page.solution %}
        identity_3d = np.array([np.eye(3) for _ in range(3)])
        print("3D Identity Matrix:\n", identity_3d)
{% endif %}

### Task 12 -- Runtime

Numpy and scipy both implement their procedures in a compiled language
such as fortran and C, rather than the interpreted language python.
Hence, whenever possible the functions of those libraries must be used
to gain efficiency. Let $A$ be a square matrix of random integer numbers
large enough. Undertake the following experimental analysis:

a)  Compare the running time to multiply $A$ by itself using the `numpy`
    and `scipy` libraries and the function you wrote in Task 4.

b)  Compare the running time to calculate the column-wise sum of the
    matrix $A$ using the base `sum` function, the `numpy.sum` function
    and with a for loop.

The easiest way to measure the execution time of a single statement is
to use IPython's magic function `%timeit`. As the execution time of a
single statement can be extremely short, the statement is placed in a
loop and executed several times (option `-n`). Moreover since other
tasks running in the computer may influence the result, the loop is
repeated a number of times and the best result is taken (option `-r`).
The best results is the minimum time.

Alternatively, one can use the module `timeit` from Python. Here the
parameter `number` and `repeat` refer to the number of times the command
to track is executed and to the number of times the experiment is
repeated, respectively.
