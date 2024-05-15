#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// proto typing
float countLetters(string text);
float countWords(string text);
float countSentences(string text);
void readerGrade(float index);

int main(void)
{
    string text = get_string("Text: ");
    // count the letters, count the words and count the sentences
    float nLetters = countLetters(text), nWords = countWords(text), nSentences = countSentences(text) || 1;

    // calculate the averages
    float L = (nLetters / nWords) * 100;
    float S = (nSentences / nWords) * 100;

    // The Coleman-Liau index
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // print out the reading grade to the screen
    readerGrade(index);
}

// count the number of letters in a given text
float countLetters(string text)
{
    int c, counter = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        c = (int) text[i];
        if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122))
        {
            counter++;
        }
    }
    return counter;
}

// count the number of words in a given text
float countWords(string text)
{
    int counter = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == ' ')
        {
            counter++;
        }
    }
    return counter + 1;
}

// count the number of sentences in a given text
float countSentences(string text)
{
    int counter = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            counter++;
        }
    }
    return counter;
}

// print out the grade for the text given
void readerGrade(float index)
{
    index = round(index);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 0 && index < 16)
    {
        printf("Grade %i\n", (int) index);
    }
    else
    {
        printf("Grade 16+\n");
    }
}
