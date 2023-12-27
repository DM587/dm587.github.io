## Sheet 2


Continue the exercises from Sheet 1 on Python programming and use the
instructor to clarify your doubts on this topic. In particular, focus
on the Tasks 13-24 on `numpy`. As you should learn from the benchmarks
in Assignment 1, you should always prefer using `numpy` to carry out linear
algebra calculations.



Exercises with a star on the side must be done
before coming to the class. Exercises with a hat on the side will be
tackled in class.



### Task 1* -- Matplotlib: Plotting in Python

Write a function to plot the curve $f(x) = \frac{1}{x-1}$ on the domain $[-2,6]$.

1. Although $f(x)$ has a discontinuity at $x=1$, a single call to `plt.plot()` in the usual way will make the curve look continuous.
Split up the domain into $[-2,1)$ and $(1,6]$.
Plot the two sides of the curve separately so that the graph looks discontinuous at $x=1$.

2. Plot both curves with a dashed magenta line.
Set the keyword argument `linewidth` (or `lw`) of `plt.plot()` to $4$ to make the line a little thicker than the default setting.

3. Use `plt.xlim()` and `plt.ylim()` to change the range of the $x$-axis to $[-2,6]$ and the range of the $y$-axis to $[-6, 6]$.


### Task 2^


Write a function that plots the functions $\sin(x)$, $\sin(2x)$,
$2\sin(x)$, and $2\sin(2x)$ on the domain $[0, 2\pi]$, each in a
separate subplot of a single figure.

1. Arrange the plots in a $2\times 2$ grid of subplots.
   
2. Set the limits of each subplot to $[0, 2\pi]\times[-2,2]$.
    (Hint: Consider using `plt.axis([xmin, xmax, ymin, ymax])` instead
    of `plt.xlim()` and `plt.ylim()` to set all boundaries
    simultaneously.)
	
3. Use `plt.title()` or `ax.set_title()` to give each subplot an appropriate title.

4. Use `plt.suptitle()` or `fig.suptitle()` to give the overall figure a title.

5. Use the following colors and line styles.
   - $\sin(x)${: green solid line.} 
   - $\sin(2x)${: red dashed line.}
   - $2\sin(x)${: blue dashed line.} 
   - $2\sin(2x)${: magenta dotted line.}




### Task 3 - Benchmarking

There are at least four methods to measure running time of functions and programs in Python.

**Method 1**
In Assignment 1, in the file `benchmark.py` you find the definition of the decorator `timer`:

```python
import time

class Timer(object):  # this is a special class: context manager
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, ty, val, tb):
        end = time.time()
        self.elapsed = end - self.start
        return False


def our_timer(repeats, loops):
    #repeats = 5
    #loops = 1000
    def decorator(func):
        def wrapper(*args, **kwargs):
            times = [0]*repeats
            for i in range(repeats):
                with Timer() as t1:
                    for _ in range(loops):
                        func(*args, **kwargs)
                times[i] = t1.elapsed
                #print(func.__name__, times[i])
            print("best of", str(repeats), "times",str(loops),"executions: ", func.__name__, str(min(times)))
        return wrapper
    return decorator
```
Then we can use the decorator to decorate the definition of our function as follows:
```
@our_timer(3, 1000)
def my_function(x, y):
    return x+y

my_function(2,4)
best of 3 times 1000 executions for my_function 0.00164079666137
```




**Method 2**
If you are working in an interactive environment (jupyter notebooks) you can achieve this task via the magic function `%timeit`:

```
In [50]: %timeit -n 50 -r 3 my_function()
50 loops, best of 3: 585 ms per loop
```
The parameter `-n` controls how many time the function is executed before measuring time (this is to minimize cache effects) and `-r` controls the number of repetitions from which the best run is reported.

**Method 3**
Method 2 can be implemented via module `timeit` also in a normal script. 
```
import timeit

experiment_1 = timeit.Timer(stmt = 'my_function()', setup = setup_statements)
```
See the documentation of this module for details on the specification of `setup_statement`.

**Method 4**
Finally, another method is via *context manager* to be used with `with`. We first construct a context manager object for measuring the elapsed time as
follows:
```
import time
class Timer:
    def __enter__(self):
        self.start = time.time()
        # return self

    def __exit__(self, ty, val, tb):
        end = time.time()
        self.elapsed=end-self.start
        print('Time elapsed {} seconds'.format(self.elapsed))
        return False
```
The `__enter__` and `__exit__` methods are what makes this class a context manager.
```
with Timer():
    my_function()
```
or if we want the timing result to be accessible in a variable, the enter method must return the
Timer instance (uncomment the return statement) and used as follows:
```
with Timer() as t1:
    find_elements_1(A)
    t1.elapsed # contains the result
```




Using the results from the benchmarking of the methods in Assignment 1, compare the
growth curve of your `list` implementation and `numpy` implementation of matrix
multiplication. Consider only square matrices of varying size. Try to
perform logarithmic transformations on the axis. Which transformation
leads to a linear growth? What do the plots say about the growth
function (ie, polynomial or exponential) of the procedures?  [You will
need to modify `benchmark.py` to print out the results for different
sizes of the matrices. You should put the results in a file. Then your
script for plotting should read the data from the file and plot the
growth curves.]

