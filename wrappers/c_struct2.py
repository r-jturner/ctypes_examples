# Import necessary modules
import ctypes as cts
from numpy.ctypeslib import as_ctypes
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
so_file = os.path.join(script_dir, '../src/lib/struct2.so')
_struct2 = cts.CDLL(so_file)

def mk_struct(arr1, arr2):
    n_length = len(arr1)
    global arr_struct
    class arr_struct(cts.Structure):
        _fields_ = [('n', cts.c_int),
                    ('mult',cts.POINTER(cts.c_double * n_length)),
                    ('div',cts.POINTER(cts.c_double * n_length))]
    #array_type = cts.c_double * n_length
    c_arr1 = as_ctypes(arr1)
    c_arr2 = as_ctypes(arr2)
    array_type = cts.c_double * n_length

    arrayManip = _struct2.arrayManip
    arrayManip.argtypes = [cts.c_int, cts.POINTER(array_type), cts.POINTER(array_type)]
    arrayManip.restype = cts.POINTER(arr_struct)

    # Run the C function using the input to the python function and then print out the results 
    test_struct = arrayManip(n_length, c_arr1, c_arr2)
    #print(test_struct[0].mult[0][:])
    #print(test_struct[0].div[0][:])
    return test_struct
