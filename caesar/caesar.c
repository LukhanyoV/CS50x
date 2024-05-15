#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// proto typing
char rotate(char c, int key);
bool only_digits(string s);

// main method
int main(int argc, string argv[])
{
    // get the last argument
    string last = argv[argc - 1];

    // validate the number of arguments
    if (argc != 2 || !only_digits(last))
    {
        printf("Usage: ./caeser key\n");
        return 1;
    }

    // convert the key to integer
    int key = atoi(last);
    // user input
    string plaintext = get_string("plaintext: ");
    string ciphertext = plaintext;

    // loop through the plain text and rotate only letters
    for (int i = 0; i < strlen(plaintext); i++)
    {
        ciphertext[i] = rotate(plaintext[i], key);
    }

    printf("ciphertext: %s\n", ciphertext);
}

// rotate letter (position + key) % 26 amount of times
char rotate(char c, int key)
{
    // check if its an alpha
    if (isalpha(c))
    {
        int offset = isupper(c) ? 65 : 97;
        // how far from a or A
        int pi = c - offset;
        // Caesar’s algorithm
        int ci = (pi + key) % 26;
        // check if its upper case
        return (char) ci + offset;
    }
    return c;
}

// check if the key is only digits
bool only_digits(string s)
{
    for (int i = 0; i < strlen(s); i++)
        if (!isdigit(s[i]))
            return false;
    return true;
}
