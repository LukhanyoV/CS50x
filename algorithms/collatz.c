#include <stdio.h>

int collatz(int n);

int main(void)
{
    int num = 10;
    int res = collatz(num);
    printf("Collatz: %i\n", res);
}

int collatz(int n)
{
    if (n == 1) return 0;
    else if (n % 2 == 0) return 1 + collatz(n / 2);
    else return 1 + collatz(3 * n + 1);
}
