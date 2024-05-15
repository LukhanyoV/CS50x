// #include <cs50.h>
#include <stdio.h>

int main(void)
{
    char stars[5] = {' ', ' ', ' ', ' ', ' '};
    char hashez[5] = {' ', ' ', ' ', ' ', ' '};

    for(int i = 0; i < 4; i++)
    {
        stars[i] = '#';
        hashez[4-i] = '*';

        printf("\t%s\n", hashez);
        // printf("%s %s %s\n", stars, hashez, hashez);
    }
}
