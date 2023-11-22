---
layout: default
mathjax: true
title:  Sheet 5
date:   2022-11-15 08:33:19 +0100
categories: exercises 
---

## Sheet 5


### Task 1

PageRank is the algorithm that Google originally used to determine the
"importance" (or rank) of a web page.

The idea for PageRank is this: Define a Markov chain that describes
the behavior of a random web-surfer. Consider the stationary
distribution of this Markov chain. Define the weight of a page to be
the probability of that page in the stationary distribution.
Higher-probability pages are considered better. So when the user
submits a query consisting of a set of words, present the web pages
containing these words, in descending order of probability.

Conveniently, the PageRank vector (the stationary distribution) does
not depend on any particular query, so it can be computed once and
then used for all subsequent queries. (Of course, Google periodically
recomputes it to take into account changes in the web.)

We start with a rudimentary Markov chain and we discover why it needs to
be improved.


#### Subtask 1.a

In each iteration, the random surfer selects an outgoing link from his
current web page, and follows that link. We consider the small Web
network of the picture, consisting of only six sites linked together as
shown.


<img src="{{ "/assets/pagerank2.png" | absolute_url }}" alt="Graph for Task
1" style="width:400px;height:250px;align:center;" class="center">

<!-- ![graph]({{ "/assets/pagerank.png" | absolute_url }}){: .center-image }

-->


Let $\delta{(j)}$ denote the number of links from page $j$ to other pages
in the network. If $\delta{(j)}\neq 0 $ and no other knowledge about the
relevance of the pages is given, then it is reasonable to assume
that the surfer follows links from the current web page with
probability:

$$a_{ij}=\begin{cases}1/\delta{(j)} & \text{if there is a link from page $j$ to page
  $i$}\\
0 & \text{otherwise}
\end{cases}$$ 


Write the transition matrix $A_1$ of the Markov chain and check that it
is indeed a *stochastic* matrix.

According to this Markov chain, how likely is that the random surfer
is at each page after many iterations? What are the most likely
pages?

Use the power method (aka, iterative method) and carry out the operations in Python for the
following cases:

- if it starts at page 6 and takes an even number of iterations

- if it starts at page 6 and takes an odd number of iterations

- if it starts at page 4 and takes an even number of iterations

- if it starts at page 4 and takes an odd number of iterations

You should find that the answer depends on where the surfer starts and
how many steps he takes.  The probabilities are almost the same except
that the probabilities of nodes 2 and 3 are swapped.


#### Subtask 1.b

From the point of view of computing definitive pageranks using the
power method, there are two things wrong with this Markov chain:

i.  There are multiple clusters in which the surfer gets stuck. One
    cluster is page 2 and page 3, and the other cluster is page 1.

ii. There is a part of the Markov chain that induces periodic behavior:
    once the surfer enters the cluster page 2 and page 3, the
    probability distribution changes in each iteration.

The first property implies that there are multiple stationary
distributions. The second property means that the `power method` might
not converge. We want a Markov chain with a unique stationary
distribution so we can use the stationary distribution as an assignment
of importance weights to web pages. We also want to be able to compute
it with the `power method`. We apparently cannot work with the Markov
chain in which the surfer simply chooses a random outgoing link in each
step.

Consider then an alternative, very simple Markov chain: the surfer
jumps from whatever page he's on to a page chosen uniformly
at random.

Write the transition matrix $A_2$ for this Markov chain. Is there a
unique stationary distribution? Which one?


#### Subtask 1.c

As you may have discovered the latter Markov chain does not in any
way reflect the structure of the Web network. Using the stationary
distribution to assign weights would provide no information at all.

Instead, we will use a mixture of these two Markov chains. That is,
we will use the Markov chain whose transition matrix is

$$A = 0.85A_1 + 0.15A_2$$

Show that the matrix $A$ is a *stochastic matrix*, that is, the sum
of the entries in all columns is 1.

The Markov chain corresponding to the matrix $A$ describes a surfer
obeying the following rule:

-   With probability 0.85, select one of the links from the current
    web page, and follow it.

-   With probability 0.15, jump to a web page chosen uniformly
    at random. (This is called teleporting in the context
    of PageRank.)

You can think of the second item as modeling the fact that sometimes the
surfer gets bored with where he/she is. However, it plays a
mathematically important role. The matrix $A$ is a positive matrix
(every entry is positive). A theorem ensures that the corresponding
Markov chain is regular, that is, there is a unique stationary
distribution, and the power method will converge to it.

Calculate how likely it is that the random surfer is at each page
after many iterations and rank consequently the pages. You can use
the theory of diagonalization or the power method and carry out the
calculation with Python.



### Task 2


The file [`top250movies.txt`]({{ "/assets/top250movies.txt" | absolute_url }}) contains data from the 250 top-rated movies according
to
[IMDb](https://www.imdb.com/search/title?groups=top_250&sort=user_rating) (scraped with
[imdbpy](https://imdbpy.sourceforge.io/)).
Each line in the file lists a movie title and its cast as
`title/actor1/actor2/...`, with the actors listed mostly in billing
order (stars first), though some casts are listed alphabetically or in
order of appearance.

Create a networkx `nx.DiGraph` object with a node for each actor in the file.
The weight from actor `a` to actor `b` should be the number of times
that actor `a` and `b` were in a movie together but actor `b` was listed
first.  That is, *edges point to higher-billed actors*.  

- Compute the PageRank values of the actors.

- Write a function to rank them

- Return the list of ranked actors.  


(Hint: Consider using `itertools.combinations()` while
constructing the graph. Also, check that the file you are reading is
stored with encoding UTF-8, since several actors and actresses have
nonstandard characters in their names such as ø and æ.)


With $\epsilon = 0.7$, the top three (most visible) actors should be
Leonardo DiCaprio, Robert De Niro, and Tom Hanks, in that order.
