import numpy as np
import sys
import os

proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(proj_root)

from wrappers import c_struct2

a = np.array([10.,20.,30.])
b = np.array([5.,4.,3.])

tmp = c_struct2.mk_struct(a,b)
print(tmp[0].mult[0][:])
print(tmp[0].div[0][:])
