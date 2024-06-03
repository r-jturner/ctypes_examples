# ctypes_examples
Welcome to the amazing world of using a language that isn't python!

Sometimes you may want to run code that's memory intensive, or you've written something that requires nested for loops and you can't be bothered to properly factorise your code - no matter!

What if you could pawn off all of the hard work to a different language, and still do all of the interesting stuff in python?

Allow me to introduce you to **ctypes!**

**ctypes** is a python library that allows you to use foreign functions (i.e. from C) within python. It gives us access to C shared libraries and data types, 
which we can then wrap in nothing but 100% python. There are other methods/tools that can be used to achieve the same thing, Cython and cffi are immediate 
comparisons. I'm not going to say which is better or worse, I found ctypes to be easy to immediately get the hang of and implement. For more involved projects
Cython or cffi may provide more flexibility or usability, I couldn't say. 

For the purposes of these examples we will need three files for each case: a C script we wish to wrap in python code, the python script that does said wrapping, 
and a third python file that calls the python wrapper.
## Files
This folder contains three other, smaller folders:
1. **main** - this folder contains all of the python scripts that we will actually run - notice how there is no mention of C at all in these files
2. **src** - this folder contains all of the C code that we want to run in python, including another folder to hold our shared objects (.so files)
   and a Makefile, more on that soon
3. **wrappers** - this folder, believe it or not, contains the python code that will wrap our C code, allowing us to run our C scripts in (what looks like) pure python
   
## Installation
1. Clone this repo by pasting the following into your terminal

        git clone https://github.com/r-jturner/ctypes_examples.git

2. Navigate to the /src/ subdirectory, and run the Makefile by typing 'make' into the terminal - you may need to modify the Makefile to match your compiler.
   This will compile the C scripts in the /src/ folder and create a shared object (.so file) for each in /src/lib/. These .so files
   are needed for ctypes to parse the compiled code.

3. Now you should have a set of four .so files in the /src/lib/ folder, and we should now be able to run any of the four python scripts in the /main/
   folder - assuming you have a python environment initialised...

## Support
For support, contact Ryan Turner (rjturner@swin.edu.au)
