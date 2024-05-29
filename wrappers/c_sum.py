# Import the cytpes module
import ctypes
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
so_file = os.path.join(script_dir, '../src/lib/sum.so')
# Load the shared library (.so for linux/mac, .dll for windows)
_sum = ctypes.CDLL(so_file)
# Set argument types for the function in the shared library '_sum'
# ctypes.POINTER(ctypes.c_int) is the python ctypes equivalent of an int * in C
# ctypes will check if the arguments we pass the the function fit these types
_sum.simple_threesum.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int)
_sum.sum_function.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))

# Define the python function wrapper for sum_function()
def sum_function(numbers):
    #State that the library is global to make it easier to find
    global _sum
    # Query the input array for its length to pass to sum_function
    num_numbers = len(numbers)
    # Define a ctypes array type compatible with the library
    # achieved by multipying ctypes.c_int with an integer
    array_type = ctypes.c_int * num_numbers
    # This type wants every element of the array as an input (so that it can be summed) 
    # and so we pass '*numbers'
    result = _sum.sum_function(ctypes.c_int(num_numbers), array_type(*numbers))
    # The C function returns an integer, and we require a python integer as we leave the function
    # and so we return an int() of the output
    return int(result)

def simple_threesum(a, b, c):
    result = _sum.simple_threesum(ctypes.c_int(a), ctypes.c_int(b), ctypes.c_int(c))
    return int(result)
