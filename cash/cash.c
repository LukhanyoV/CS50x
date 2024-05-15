#include <cs50.h>
#include <stdio.h>

#define PENNY 1
#define NICKEL 5
#define DIME 10
#define QUARTER 25

int main(void)
{
    int change;
    do {
        change = get_int("Change owed: ");
    } while (change < 0);
    int coins = 0;
    while (change  > 0){
        if (change >= QUARTER) change -= QUARTER;
        else if (change >= DIME) change -= DIME;
        else if (change >= NICKEL) change -= NICKEL;
        else if (change >= PENNY) change -= PENNY;
        coins++;
    }
    printf("%i\n", coins);
}


/*
1. Ask for change owed
2. Initialize coins as 0
3. Initialize quarter as 25
4. Initialize dime as 10
5. Initialize nickel as 5
6. Initialize penny as 1
7. While change greater than 0:
8.    if change is greater or equal to quater:
9.        subtract a quarter from the change
10.   else if change is greater or equal to dime
11.       subtract a dime from the change
12.   else if change is greater or equal to nickel
13.       subtract nickel from change
14.   else if change is greater or equal to penny
15.       subtract penny from change
16.   increment count of coins used
17. Print out number of coins used
*/
