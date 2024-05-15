#include <cs50.h>
#include <stdio.h>

int main(void){
    int n = get_int("Height: ");
    for(int i = 1; i <= n; i++)
    {
        // print the indent
        for(int j = n; j >= i; j--)
        {
            printf(" ");
        }
        // print pyramid
        for(int j = 0; j < i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
}
