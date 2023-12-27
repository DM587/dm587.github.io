
## Sheet 1


Before the exercise class make sure you have gone through the colab
posted on the web page.  Exercises with a star on the side must be done
before coming to the class.  Exercises with a hat on the side will be
tackled in class. The others are left for self study.



### Task 1*  -  Functions


The volume of a sphere with radius $r$ is $V = \frac{4}{3}\pi r^3$.  In
a Python file, define a function called `sphere_volume()` that accepts a
single parameter $r$ and returns the volume of the sphere of radius $r$,
using $3.14159$ as an approximation for $\pi$ (alternatively look for
its value in the module `math`).  Also write an appropriate docstring
for your function. Try keeping the body of the function down to a single
line of code.

To test your function, call it under the `if __name__ == "__main__"`
clause and print the returned value.  Run your file to see if your
answer is what you expect it to be.


### Task 2  -  Printing

The built-in `print()` function has the useful keyword arguments `sep` and `end`.
It accepts any number of positional arguments and prints them out with
`sep` inserted between values (defaulting to a space), then prints `end`
(defaulting to the *newline character* `'\n'`).
```python
>>> print(1, 2, 3, sep=', ', end='!\n')
1, 2, 3!
```

Write a function called `isolate()` that accepts five arguments, prints
the first three separated by 5 spaces, then prints the rest with a single
space between each output.  For example, 

```python 
>>> isolate(1, 2, 3, 4, 5) 
1     2     3 4 5 
```


### Task 3*  -  Slicing strings

Write two new functions, called `first_half()` and `backward()`.

1. `first_half()` should accept a parameter and return the first half of it, excluding the middle character if there is an odd number of characters.
(Hint: the built-in function `len()` returns the length of the input.)
2. The `backward()` function should accept a parameter and reverse the
order of its characters using slicing, then return the reversed string. (Hint: The `step` parameter used in slicing can be negative.)

Use IPython to quickly test your syntax for each function.



### Task 4*  -  Lists

Write a function called `list_ops()`.
Define a list with the entries `"bear"`, `"ant"`, `"cat"`, and `"dog"`, in that order.
Then perform the following operations on the list:

1. Append `"eagle"`.
2. Replace the entry at index 2 with `"fox"`.
3. Remove (or pop) the entry at index 1.
4. Sort the list in reverse alphabetical order.
5. Replace `"eagle"` with `"hawk"`. (Hint: the list's `index(val)` method may be helpful.)
6. Add the string `"hunter"` to the last entry in the list.

Return the resulting list.

Work out (on paper) what the result should be, then check that your function returns the correct list.
Consider printing the list at each step to see the intermediate results.


### Task 5  -  Strings

Write a function called `pig_latin()`.
Accept a parameter `word`, translate it into Pig Latin, then return the translation.
Specifically, if `word` starts with a vowel, add `"hay"` to the end; if `word` starts with a consonant, take the first character of `word`, move it to the end, and add `"ay"`.
(Hint: use the `in` operator to check if the first letter is a vowel.)



### Task 6*

This problem originates from (https://projecteuler.net), an excellent resource for math-related coding problems.

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is $9009 = 91 \times 99.$
Write a function called `palindrome()` that finds and returns the
largest palindromic number made from the product of two 3-digit numbers.



### Task 7^

The alternating harmonic series is defined as follows.

\\[\sum_{n=1}^\infty \frac{(-1)^{(n+1)}}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \ldots = \ln(2)\\]

Write a function called `alt_harmonic()` that accepts an integer $n$.
Use a list comprehension to quickly compute the first $n$ terms of this series (be careful not to compute only $n-1$ terms).
The sum of the first 500,000 terms of this series approximates $\ln(2)$
to five decimal places. (Hint: consider using Python's built-in `sum()` function.)


### Task 8^  -  Lists

Write a function that accepts a list $L$ and returns the minimum,
maximum, and average of the entries of $L$ (in that order).  Can you
implement this function in a single line?


### Task 8b^  -  List comprehension

Write the inverse of the function that associates the names "Marco",
"Luca", "Alex" to the numbers 1, 2, 3 respectively.


### Task 9^  -  Mutable vs Immutable Objects 

Determine which of Python's object types are mutable and which are immutable by repeating the following experiment for an `int`, `str`, `list`, `tuple`, and `set`.

1. Create an object of the given type and assign a name to it.
2. Assign a new name to the first name.
3. Alter the object via only one of the names (for tuples, use `my_tuple += (1,)`).
4. Check to see if the two names are equal (compare also the identity/address of
    the object they refer to via the function `id()`).
    If they are, then since changing one name changed the other, the names refer to the same object and the object type is mutable.
    Otherwise, the names refer to different objects---meaning a new object was created in step 2---and therefore the object type is immutable.

For example, the following experiment shows that `dict` is a mutable type.
```python
>>> dict_1 = {1: 'x', 2: 'b'}           # Create a dictionary.
>>> dict_2 = dict_1                     # Assign it a new name.
>>> dict_2[1] = 'a'                     # Change the 'new' dictionary.
>>> dict_1 == dict_2                    # Compare the two names.
 True                                   # Both names changed!
```
Print a statement of your conclusions that clearly indicates which object types are mutable and which are immutable.



### Task 10  -  Implementing Modules

Create a module called `calculator.py`.
Write a function that returns the sum of two arguments and a function that returns the product of two arguments.
Also use `import` to add the `sqrt()` function from the `math` module to the namespace.
When this file is either run or imported, nothing should be executed.

In your solution script, import your new custom module.
Write a function that accepts two numbers representing the lengths of the sides of a right triangle.
Using only the functions from `calculator.py`, calculate and return the length of the hypotenuse of the triangle.




### Task 11 - Modules

In IPython explore the modules: 
- `itertools`
- `sys`
- `random`
- `time`


### Task 12^ - Module Itertools


The *power set* of a set $A$, denoted $\mathcal{P}(A)$ or $2^A$, is
the set of all subsets of $A$, including the empty set $\emptyset$ and
$A$ itself.  For example, the power set of the set $A = \\{a, b, c\\}$ is
$2^A = \\{\emptyset, \\{a\\}, \\{b\\}, \\{c\\}, \\{a,b\\}, \\{a,c\\}, \\{b,c\\},
\\{a,b,c\\} \\}$.

Write a function that accepts an iterable $A$.  Use an `itertools`
function to compute the power set of $A$ as a list of sets (why couldn't
it be a set of sets in Python?). (Hint: The power set of a set with
$n$ elements should have exactly $2^n$ elements.)




### Task 13^  -  Classes

Expand the <span>`Backpack`</span> class from the file
[object_oriented.py]({{ "/assets/object_oriented.py" | absolute_url }})
to match the following specifications.

1.  Modify the constructor so that it accepts three total arguments:
    <span>`name`</span>, <span>`color`</span>, and
    <span>`max_size`</span> (in that order). Make
    <span>`max_size`</span> a keyword argument that defaults to $5$.
    Store each input as an attribute.

2.  Modify the <span>`put()`</span> method to check that the backpack
    does not go over capacity. If there are already
    <span>`max_size`</span> items or more, print “No Room!” and do not
    add the item to the contents list.

3.  Write a new method called <span>`dump()`</span> that resets the
    contents of the backpack to an empty list. This method should not
    receive any arguments (except <span>`self`</span>).

4.  Documentation is especially important in classes so that the user
    knows what an object’s attributes represent and how to use methods
    appropriately. Update (or write) the docstrings for the
    <span>`__init__()`</span>, <span>`put()`</span>, and
    <span>`dump()`</span> methods, as well as the actual class docstring
    (under <span>`class`</span> but before <span>`__init__()`</span>) to
    reflect the changes from parts 1-3 of this problem.

To ensure that your class works properly, write a test function outside
outside of the <span>`Backpack`</span> class that instantiates and
analyzes a <span>`Backpack`</span> object.

    def test_backpack():
        testpack = Backpack("Barry", "black")       # Instantiate the object.
        if testpack.name != "Barry":                # Test an attribute.
            print("Backpack.name assigned incorrectly")
        for item in ["pencil", "pen", "paper", "computer"]:
            testpack.put(item)                      # Test a method.
        print("Contents:", testpack.contents)
        # ...


### Task 14  –  Inheritance

In [object_oriented.py]({{ "/assets/object_oriented.py" | absolute_url
}}) write a <span>`Jetpack`</span> class that inherits from the
<span>`Backpack`</span> class.

1.  Override the constructor so that in addition to a name, color, and
    maximum size, it also accepts an amount of fuel. Change the default
    value of <span>`max_size`</span> to $2$, and set the default value
    of fuel to $10$. Store the fuel as an attribute.

2.  Add a <span>`fly()`</span> method that accepts an amount of fuel to
    be burned and decrements the fuel attribute by that amount. If the
    user tries to burn more fuel than remains, print “Not enough fuel!”
    and do not decrement the fuel.

3.  Override the <span>`dump()`</span> method so that both the contents
    and the fuel tank are emptied.

4.  Write clear, detailed docstrings for the class and each of
    its methods.

### Task 15  –  Magic Methods

Endow the <span>`Backpack`</span> class from the file [object_oriented.py]({{ "/assets/object_oriented.py" | absolute_url
}}) that you have been developing in the two previous tasks with two additional magic
methods:

1.  The <span>`__eq__()`</span> magic method is used to determine if two
    objects are equal, and is invoked by the <span>`==`</span> operator.
    Implement the <span>`__eq__()`</span> magic method for the
    <span>`Backpack`</span> class so that two <span>`Backpack`</span>
    objects are equal if and only if they have the same name, color, and
    number of contents.

2.  The <span>`__str__()`</span> magic method returns the string
    representation of an object. This method is invoked by
    <span>`str()`</span> and used by <span>`print()`</span>. Implement
    the <span>`__str__()`</span> method in the <span>`Backpack`</span>
    class so that printing a <span>`Backpack`</span> object yields the
    following output (that is, construct and return the
    following string).

        <<Owner:      <name>
        Color:      <color>
        Size:       <number of items in contents>
        Max Size:   <max_size>
        Contents:   [<item1>, <item2>, ...]>>

    (Hint: Use the tab and newline characters <span>`'\\t'`</span> and
    <span>`'\\n'`</span> to align output nicely.)


### Task 16^  -  Handling Exceptions

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

### Task 17^  -  File Input/Output

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

### Task 18^  -  Matrix Multiplication in Numpy

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

### Task 19^  -  Matrix Multiplication

Write a function that defines the following matrix as a NumPy array.

$$A = \left[\begin{array}{rrr}
3 & 1 & 4\\
1 & 5 & 9 \\
-5 & 3 & 1 \end{array}\right]$$ 

Return the matrix $-A^3 + 9A^2 - 15A$.

In this context, $A^2 = AA$ (the matrix product, not the component-wise
square). The somewhat surprising result is a demonstration of the
Cayley-Hamilton theorem.

### Task 20^  -  Array Creation

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

### Task 21^  -  Arrays

Write a function that accepts a single array as input. Make a copy of
the array, then use fancy indexing to set all negative entries of the
copy to $0$. Return the copy.

### Task 22  -  Arrays

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

### Task 23^  -  Arrays

A matrix is called *row-stochastic* if its rows each sum to $1$.
Stochastic matrices are fundamentally important for finite discrete
random processes and some machine learning algorithms.

Write a function than accepts a matrix (as a 2-D array). Divide each row
of the matrix by the row sum and return the new row-stochastic matrix.
Use array broadcasting and the <span>`axis`</span> argument instead of a
loop.

(Similarly, a matrix is called *column-stochastic* if its columns each sum to $1$.)


### Task 24  -  Polynomials

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
