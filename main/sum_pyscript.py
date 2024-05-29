import numpy as np
import sys
import os

proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(proj_root)

from wrappers import c_sum

a = np.arange(10) #sum numbers from 1 to 9
print(c_sum.sum_function(a))

x,y,z = 5,10,15
print(c_sum.simple_threesum(x,y,z)) #sum the integers x, y and z 