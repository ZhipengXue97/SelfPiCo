# Extracted from https://stackoverflow.com/questions/568962/how-do-i-create-an-empty-array-and-then-append-to-it-in-numpy
from numpy import *
a = array([10,20,30])
append(a, [[1,2,3]], axis=0)
array([[10, 20, 30],      
       [1, 2, 3]])

append(a, [[15],[15]], axis=1)
array([[10, 20, 30, 15],      
       [1, 2, 3, 15]])

