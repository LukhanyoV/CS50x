#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prompt the user for a name
    string name = get_string("What is your name? ");
    // print out a greeting to the user
    printf("Hello, %s\n", name);
}
