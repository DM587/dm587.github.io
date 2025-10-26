
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

To test your function, call it under the `if __name__ == "__main__"` clause and
print the returned value.  Run your file to see if your answer is what you
expect it to be.  Remember to use type annotations to define parameters and
outputs of your functions in this and in the following exercises.

### Task 1b

Write a list of the first 100 numbers in which any number divisible by
three is replaced by the word "fizz" and any divisible by five by the
word "buzz". Numbers divisible by both become "fizz buzz". Can you
create a numpy array containing this list?

{% if page.solution %}

```{python}
    for num in range(1,100):
      if num % 5 == 0 or num % 3 == 0:
        print("fizzbuzz")
      elif num % 5 == 0:
        print("buzz")
      elif num % 3 == 0:
        print("fizz")
      else:
        print(num)
```

{% endif %}

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

Write two new functions manipulating strings, called `first_half()` and `backward()`.

1. `first_half()` should accept a parameter and return the first half of it,
excluding the middle character if there is an odd number of characters.  (Hint:
the built-in function `len()` returns the length of the input.)
2. The `backward()` function should accept a parameter and reverse the order of
its characters using slicing, then return the reversed string. (Hint: The `step`
parameter used in slicing can be negative.)

Use IPython/Jupyter to quickly test your syntax for each function.


### Task 4a* -- Data Types

Revise the difference between the main data types in Python: list,
tuples, dictionaries and sets. Write an example for each of them in
which you define and initialize a variable for each type and then print
the content looping through the elements of the variable.

<!-- Numpy arrays can only contain data of the same type hence we cannot
create an array from a list containing both numbers and strings.
-->

{% if page.solution %}
```
    # lists my_list = [10,20,30,40,50,60] for i in my_list: print(i)

    # tuples
    my_tuple = (1,2,3,4,5,6,7,8,9)
    for i in my_tuple:
      print(i)

    # dictionaries
    my_dict = {'name': 'Esau', 'age': 2, 'occupation': 'My dog'}
    for key,val in my_dict.iteritems():
      print("My {} is {}".format(key,value))

    # set
    my_set = {20,30,40,50,60,20,30,40,50}
    for i in my_set:
      print(i)
```

{% endif %}

### Task 4b  -  Lists

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


### Task 4c -- One liner quizzies

Write a one line Python code for the following tasks:

a)  Construct the set $S=\{x \in \mathbb{R} \mid x\geq 0 \land x \bmod
      3 \equiv 1 \}$

{% if page.solution %}
        S = {x for x in range(50) if x % 3 == 1}
{% endif %}

b)  Using list comprehension make a list for $\{(i,j) \mid i\in
      \{1,2,3,4\}, j \in \{5,7,9\}\}$

{% if page.solution %}
        [(i,j) for i in (1,range(4)+1) for j in [5,7,9]]
{% endif %}

c)  Calculate the inverse of a function or the index function for an
    invertible function (ie, bijective = injective + surjective) given
    in form of a dictionary.

{% if page.solution %}
        {d[k]:k for k in d}
        {v:k for k,v in d.items()}
{% endif %}

d)  What is the result of the following lines?

```
map(lambda x: x%3, range(5))
list(filter(lambda x: x%2==0, range(5)))
```

### Task 5  -  Strings

Write a function called `pig_latin()`.  Accept a parameter `word`, translate it
into Pig Latin, then return the translation.  Specifically, if `word` starts
with a vowel, add `"hay"` to the end; if `word` starts with a consonant, take
the first character of `word`, move it to the end, and add `"ay"`.  (Hint: use
the `in` operator to check if the first letter is a vowel.)

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


### Task 9^  -  List comprehension

Write the inverse of the function that associates the names "Marco",
"Luca", "Alex" to the numbers 1, 2, 3 respectively.

### Task 10^  -  Mutable vs Immutable Objects 

Determine which of Python's object types are mutable and which are immutable by
repeating the following experiment for an `int`, `str`, `list`, `tuple`, and
`set`.

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

### Task 11  -  Implementing Modules

Create a module called `calculator.py`.
Write a function that returns the sum of two arguments and a function that returns the product of two arguments.
Also use `import` to add the `sqrt()` function from the `math` module to the namespace.
When this file is either run or imported, nothing should be executed.

In your solution script, import your new custom module.
Write a function that accepts two numbers representing the lengths of the sides of a right triangle.
Using only the functions from `calculator.py`, calculate and return the length of the hypotenuse of the triangle.

### Task 12 - Modules

In IPython explore the modules: 
- `itertools`
- `sys`
- `random`
- `time`

### Task 13^ - Module Itertools

The *power set* of a set $A$, denoted $\mathcal{P}(A)$ or $2^A$, is
the set of all subsets of $A$, including the empty set $\emptyset$ and
$A$ itself.  For example, the power set of the set $A = \\{a, b, c\\}$ is
$2^A = \\{\emptyset, \\{a\\}, \\{b\\}, \\{c\\}, \\{a,b\\}, \\{a,c\\}, \\{b,c\\},
\\{a,b,c\\} \\}$.

Write a function that accepts an iterable $A$ and uses an `itertools`
function to compute the power set of $A$ as a list of sets (why couldn't
it be a set of sets in Python?). (Hint: The power set of a set with
$n$ elements should have exactly $2^n$ elements.)

### Task 14^  -  Classes

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


### Task 15  –  Inheritance

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

### Task 16  –  Magic Methods

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


### Task 17 - Calculate Greek pi

Write a program to calculate Greek pi by Monte Carlo Simulation.

### Task 18 - Monty Hall Problem

The Monthy Hall Problem is as follows. Suppose you're on a game show, and you're
given the choice of three doors: Behind one door is a car; behind the others,
goats. You pick a door, say No. 1, and the host, who knows what's behind the
doors, opens another door, say No. 3, which has a goat. He then says to you, "Do
you want to pick door No. 2?" Is it to your advantage to switch your choice?

You can consult the wikipedia page on this problem to see if your answer is
correct. Here, you have to implement a small program to answer the question by
simulation.