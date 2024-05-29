#include <stdlib.h>

typedef struct arr_struct{
    int n;
    double *mult;
    double *div;
} arr_struct;

arr_struct *arrayManip(int n, double *arr1, double *arr2){
    arr_struct *out = malloc(sizeof *out);
    out->n = n;
    out->mult = malloc(n*sizeof out->mult[0]);
    out->div = malloc(n*sizeof out->div[0]);
    for(int i = 0; i < n; i++){
        out->mult[i] = arr1[i] * arr2[i];
        out->div[i] = arr1[i] / arr2[i];
    }
    return out;
}

/* gcc -fPIC -shared -o libstruct2.so struct2.c */