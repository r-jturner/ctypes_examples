import sys
import os
import numpy as np

proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(proj_root)

from wrappers import c_double

a = np.array([[1.,2.,3.],[4.,5.,6.]])

print(c_double.double_function(a))