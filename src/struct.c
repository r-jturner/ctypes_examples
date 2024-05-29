#include <stdlib.h>
/* 
Playing around with structs now, these are similar to classes in python
but only define parameters and don't have associated functions. If we did want 
to write functions that operate on structs they must be written such that they 
accept structs as a parameter
*/
typedef struct my_struct{
    int n; /* integer describing the length of the array arr*/
    double *arr; /* A pointer for the array, containing double-type elements */
} my_struct;
/* 
'typedef' keyword helps to avoid clutter later on, i.e. here we can now type
'my_struct <name>', rather than 'struct my_struct <name>'.
If our structure has a complicated type (pointer or some ND array, etc.) then this shorthand 
can declutter code. Also consider the case where we are constantly reusing a specific type of
variable, like a pointer to a float, we could give this an alias via 'typedef float* fptr'.
*/
my_struct *new_struct(int n){
    /*
    We don't know the size of the array we want beforehand, and so the memory required 
    needs to be dynamically allocated. We first allocate memory for the struct itself,
    and then, given the user input, allocate memory to our array 
    */
    my_struct *out = malloc(sizeof *out);
    /* Assign the user input to the 'n' variable of my_struct*/
    out->n = n;
    /* Allocate sufficient memory to hold the elements of our array*/
    out->arr = malloc(n*sizeof out->arr[0]);
    /* Iterate through i from 0 to n and place i in that element of the array*/
    for(int i = 0; i < n; i++){
        out->arr[i] = i;
    }
    return out;
}

/* gcc -fPIC -shared -o libstruct.so struct.c */