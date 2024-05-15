#include <cs50.h>
#include <ctype.h> //to-upper
#include <stdio.h>
#include <string.h> // str-len

// prototyping
int getPlayerScore(string scrabble);

// global variables
// const char chars[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
const int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
long charsLen = 26;

// main method
int main(void)
{
    string player1 = get_string("Player 1: ");
    string player2 = get_string("Player 2: ");

    // if p1 > p2 then
    //      player 1 wins
    // else then
    //      if p1 < p2 then
    //          player 2 wins
    //      else then
    //          tie
    printf("%s\n", getPlayerScore(player1) > getPlayerScore(player2) ? "Player 1 wins!" : getPlayerScore(player1) < getPlayerScore(player2) ? "Player 2 wins!" : "Tie!");
}

// get the score from the scrabble
// int getPlayerScore(string scrabble)
// {
//     long scrabbleLen = strlen(scrabble);
//     int scrabbleScore = 0;

//     // loop through player 1 word
//     for (int i = 0; i < scrabbleLen; i++)
//     {
//         // loop through letters in alphabet
//         for (int j = 0; j < charsLen; j++)
//         {
//             // check if the letters match
//             if (toupper(scrabble[i]) == chars[j])
//             {
//                 // update the score for player 1
//                 scrabbleScore += points[j];
//                 // no need to check all the letters
//                 break;
//             }
//         }
//     }

//     return scrabbleScore;
// }

// get the score from the scrabble
int getPlayerScore(string scrabble)
{
    long scrabbleLen = strlen(scrabble);
    int scrabbleScore = 0;

    // loop through player 1 word
    for (int i = 0; i < scrabbleLen; i++)
    {
        if(!isalpha(scrabble[i])) continue;
        int magicIndex = toupper(scrabble[i]) - 65;
        scrabbleScore += points[magicIndex];
    }

    return scrabbleScore;
}
