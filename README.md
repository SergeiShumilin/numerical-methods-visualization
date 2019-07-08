# numerical-methods-visualization
**Numerical-methods-visualization** is intended to combine efficient implementation of numerical methods
with clear and nice looking visualization of process of finding a root.

Projects python version: 2.7

Modules needed: numpy, matplotlib

Advantages of the project:
- Simple implementation of numerical methods
- Simple visualization with matplotlib
- Finding discontinuous functions
- Easy statistics

## Quickstart

Currentely there are two methods supported
1. Bisection
2. False position

In order to use them the next syntax is used:
```
from numerical-methods-visualization.numerical_methods import bisection
from numerical-methods-visualization.numerical_methods import false_position
```
```
numerical-methods-visualization.numerical_methods.**bisection**(*f, a, b, delta_x=10e-5, delta_y=10e-5, show_iter_info=False*)

Parameters:

f             :  function

a, b          :  borders to find the root

delta_x       :  accuracy when converging in x

delta_y       :  accuracy when converging in y

show_iter_info : display iterative process in console
```
