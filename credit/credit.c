#include <cs50.h>
#include <stdio.h>

int checkVisa(long credit);
int checkAmericanExpress(long credit);
int checkMasterCard(long credit);
int getLength(long credit);

int main(void)
{
    long credit = get_long("Number: ");
    int doubles = 0, skipped = 0;
    long mod = 10, div = 1;

    int count = 0, current;

    // luhn algorithm to verify credit card
    int length = getLength(credit);
    while (count < length)
    {
        current = (credit % mod) / div;
        if (count % 2)
        {
            current *= 2;
            if (current > 9)
            {
                doubles += current % 10;
                doubles += current / 10;
            }
            else
            {
                doubles += current;
            }
        }
        else
        {
            skipped += current;
        }
        mod *= 10, div *= 10;
        count++;
    }

    // check if valid credit card
    if ((doubles + skipped) % 10 == 0)
    {
        // check type of credit card
        if (checkVisa(credit))
            printf("VISA\n");
        else if (checkAmericanExpress(credit))
            printf("AMEX\n");
        else if (checkMasterCard(credit))
            printf("MASTERCARD\n");
        // credit card passed the luhn algorithm but dont know which type
        else
            printf("INVALID\n");
    }
    // invalid credit card
    else
    {
        printf("INVALID\n");
    }
}

// method to check if credit card is visa
int checkVisa(long credit)
{
    int length = getLength(credit);
    while (credit > 10)
    {
        credit /= 10;
    }
    return credit == 4 && (length == 13 || length == 16);
}

// method to check if credit card is mastercard
int checkMasterCard(long credit)
{
    int length = getLength(credit);
    while (credit > 100)
    {
        credit /= 10;
    }
    return credit >= 51 && credit <= 55 && length == 16;
}

// method to check if credit card is american express
int checkAmericanExpress(long credit)
{
    int length = getLength(credit);
    while (credit > 100)
    {
        credit /= 10;
    }
    return (credit == 34 || credit == 37) && length == 15;
}

// get the length of digits in credit
int getLength(long credit)
{
    int count = 0;
    while (credit != 0)
    {
        credit /= 10;
        count++;
    }
    return count;
}
