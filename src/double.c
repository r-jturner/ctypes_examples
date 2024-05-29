void double_function( int m, int n, double input[m][n], double output[m][n])
{
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            output[i][j] = 2 * input[i][j];
        }
    }
}

/* gcc -fPIC -shared -o libdouble.so doube.c */