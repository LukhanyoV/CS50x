#include <stdio.h>

int main(void)
{
    int num;
    printf("Get num of steps: ");
    scanf("%i", &num);

    for(int i = 0; i < num; i++)
    {
        for(int j = 0; j <= i; j++)
        {
            printf("*");
        }
        printf("\n");
    }

}
