#include <stdio.h>

int fibonacci(int n);

int main(void)
{
    int num = 5;
    int fib = fibonacci(num);
    printf("Fibonacci of %i is %i\n", num, fib);
}

int fibonacci(int n)
{
    if (n < 2) return n;
    else return (fibonacci(n - 1) + fibonacci(n - 2));
}
