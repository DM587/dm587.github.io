## Sheet 1

### Task 1

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

### Task 2 -- Data Types

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

### Task 3 -- Python: One liner quizzies

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
