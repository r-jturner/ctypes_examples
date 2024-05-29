import sys
import os

proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(proj_root)

from wrappers import c_struct

n = 25
c_struct.mk_struct(n)