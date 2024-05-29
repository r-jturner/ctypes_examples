# import modules needed
import ctypes
import numpy as np
# we can use as_ctypes if we aren't trying to create a very specific C type
from numpy.ctypeslib import as_ctypes
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
so_file = os.path.join(script_dir, '../src/lib/double.so')
_double = ctypes.CDLL(so_file)

def double_function(arr):
    # Depending on the use case we may or may not need to declare the library globally
    # or ensure that our inputs are in C contiguous memory
    global _double
    arr = np.ascontiguousarray(arr)
    # But sometimes we definitely do!
    #arr = np.matrix.transpose(arr)
    #arr = np.ascontiguousarray(arr)
    # as_ctypes coverts the numpy array to a C array
    c_arr = as_ctypes(arr)
    # Can also check the ctypes object made from arr
    print("c_arr is a ctypes object that has the type", arr.ctypes.shape)
    # using the characteristics of the input we can derive our other int inputs
    nrow = arr.shape[0]
    ncol = arr.shape[1]
    # define an empty array to store our results
    out = np.empty([nrow,ncol], dtype=np.float64)
    # using as_ctypes as above
    c_out = as_ctypes(out)
    # C functions may also expect a pointer to a data type as a parameter in order to write to 
    # its location in memory (or if data is too large) 
    # Using byref() we can pass parameters by reference rather than by value, does
    # the same job as pointer() but without constructing an actual pointer object in python
    result = _double.double_function(ctypes.c_int(nrow), ctypes.c_int(ncol), 
                                     ctypes.byref(c_arr), ctypes.byref(c_out))
    return out
