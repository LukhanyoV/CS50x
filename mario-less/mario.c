#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ask the user  for a number from 1 - 8
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int i = 0; i < height; i++)
    {
        // print out the spaces
        for (int j = height - 1; j > i; j--)
        {
            printf(" ");
        }
        // print out the triangle
        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }

        // add the separator
        printf("  ");

        // print out the secondd triangle
        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}

