#include <stdio.h>

int main(void)
{
    int num = 5;
    //-- print square by x-by-y
    // int x = 4;
    // int y = 5;

    // for (int i = 0; i < x; i++)
    // {
    //     for (int j = 0; j < y; j++)
    //     {
    //         printf("#");
    //     }
    //     printf("\n");
    // }

    for(int i = 0; i < num; i++)
    {
        for(int j = num; j >= i; j--)
        {
            printf(" ");
        }
        for(int k = 0; k <= i; k++)
        {
            printf("*");
            printf("*");
        }
        printf("\n");
    }

}
