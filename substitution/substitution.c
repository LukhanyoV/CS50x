#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// proto typing
string substite(string plaintext, string key);
bool only_alpha(string s);
bool check_duplicates(string s);

// main method
int main(int argc, string argv[])
{
    // get the last argument
    string key = argv[argc - 1];

    // validate the number of arguments
    // validate the key length
    // validate the key only has alpha
    // validate the key for duplicates
    if (argc != 2 || strlen(key) != 26 || !only_alpha(key) || check_duplicates(key))
    {
        printf("Usage: ./substitution key\n");
        printf("The key has to be unique alphabets of length 26\n");
        return 1;
    }

    // user input
    string plaintext = get_string("plaintext: ");
    // perform the substitution
    string ciphertext = substite(plaintext, key);

    printf("ciphertext: %s\n", ciphertext);
}

// rotate letter (position + key) % 26 amount of times
string substite(string plaintext, string key)
{
    // clone for now to make the lengths the same
    string ciphertext = plaintext;
    //
    int position;
    //
    char current;
    for (int i = 0; i < strlen(plaintext); i++)
    {
        // save current plaintext character
        current = plaintext[i];
        // if its an alphabetic character you can substitute
        if (isalpha(plaintext[i]))
        {
            // get the index to substitute with
            position = isupper(current) ? current - 65 : current - 97;
            // substitute while keeping original case
            ciphertext[i] = isupper(current) ? toupper(key[position]) : tolower(key[position]);
        }
        // if its not an alphabetic character dont substitute
        else
        {
            ciphertext[i] = plaintext[i];
        }
    }
    return ciphertext;
}

// check if the key is only alphabets
bool only_alpha(string s)
{
    for (int i = 0; i < strlen(s); i++)
        if (!isalpha(s[i]))
            return false;
    return true;
}

// check for duplicates
// return 1 if duplicates exist else 0
bool check_duplicates(string s)
{
    // loop through the characters of the key
    for (int i = 0; i < strlen(s); i++)
    {
        // looping through the characters of the key
        // to be able to check for duplicates
        for (int j = 0; j < strlen(s); j++)
        {
            // check if the characters are the same
            // and not in the same position\
            // to upper case just in case user gives mixed case key
            if (toupper(s[i]) == toupper(s[j]) && i != j)
            {
                return 1;
            }
        }
    }
    // return false if no duplicates found
    return 0;
}
