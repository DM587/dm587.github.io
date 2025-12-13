---
layout: default
mathjax: true
title:  asg-linprog
script:  linprog.py
date:   2025-12-10 09:10:49 +0100
categories: assignments
---

#### Assignment: Linear Programing and Affine Scaling

**_Submission Deadline: Thursday, December 18, 2025, at 12_**

This assignment is optional. If you submit it, then the 6 best of your 7
submitted assignments will be counted towards your final grade.

The script that you have to edit and submit before the deadline is
`asg-linprog/linprog.py`. 

You will have to implement the affine scaling algorithm for solving linear
programs as described in the lecture.  Moreover you will have to implement and
solve a model for the diet problem. This problem consists in finding the amounts
of a set of food items that minimize cost while satisfying certain minimal and
maximal nutritional requirements. The data for the food items and their nutritional
values are provided in the script file. Different data sets will be used in the
remote testing system. 

In all computational examples, use the unitary vector as initial point but be
aware that this might not be feasible and that you will need to address this
issue in your implementation.  Overall, use the default tolerance of 1e-3. 

Other instructions are provided in the docstrings of `asg-linprog/linprog.py`.
Otherwise write to the teacher. This assignment has not been tested thoroughly.
If you find any issues, please report them as soon as possible.

#### Errata Corrigenda

- December 13, 2025, 15:00: In the script `asg-linprog/linprog.py` the test on
  line 267 has to be changed into:
  ```
  (7.183238, array([0.000001, 0.731094, 3.380249, 0.      , 0.000001]))
  ```
  If you are using python 3.13 or above you might need to adjust the first value
  to:
  ```
  (np.float64(7.183238), array([0.000001, 0.731094, 3.380249, 0.      , 0.000001]))
  ```
