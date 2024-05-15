#include <stdio.h>

int factorial(int n);

int main(void)
{
    int num = 5;
    int fact = factorial(num);
    printf("Factorial of %i is %i\n", num, fact);
}

int factorial(int n)
{
    return (n == 1) ? 1 : n * factorial(n - 1);
}
