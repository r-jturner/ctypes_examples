# Import necessary modules
import ctypes as cts
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
so_file = os.path.join(script_dir, '../src/lib/struct.so')
_struct = cts.CDLL(so_file)

# Now that we're working with structures, which are user-defined, we need a way
# to properly handle these objects in python. Luckily they are similar to classes!
# Since our structure contains an array that needs to be dynamically allocated memory, 
# we cannot pre-define the class outside of our function, since we wouldn't know how large
# the array should be - thankfully we can still do so within a python function!
def mk_struct(n):
    # python wrapper function for our c code that takes an integer 'n' defining the length of a
    # one-dimensional array, constructs a class based on that integer and prints each element
    # of the resulting array

    # Through ctypes we can call a generic structue class via ctypes.Structure
    # Each subclass we define should (I'm not sure if it's 100% required or enforced) also
    # define a '_fields_' descriptor that contains a field name and field type.
    # This attribute (if used) must be a list of 2-tuples, and the types must be from ctypes.
    class my_struct(cts.Structure):
        _fields_ = [('n', cts.c_int),
                    ('arr',cts.POINTER(cts.c_double * n))]
        # In the above line we've defined the 'arr' field, corresponding to the 'arr' variable in 
        # our C struct, and because we now know how long our array is (thanks to the user) we can
        # finally declare the type - a set of 'n' C double pointers

    # Pass the C function to variable 'new_struct', so now when we want to use the function
    # we can just call this variable rather than messing with the '_struct' object
    # We also define the argument type here as well as the result type, and we've declared that
    # the output of this function should take the form of a pointer to our new class 'my_struct'
    new_struct = _struct.new_struct
    new_struct.argtypes = [cts.c_int]
    new_struct.restype = cts.POINTER(my_struct)

    # Run the C function using the input to the python function and then print our the results 
    # as a list 
    test_struct = new_struct(n)
    print(test_struct.contents.arr[0]) # why does this print statement not give us the expected result?
    print(test_struct[0].arr[0][:])
