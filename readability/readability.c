/* Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  */

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);


int main(void)
{
    string text = get_string("Text: ");
    int words = count_words(text);
    int letters = count_letters(text);
    int sentences = count_sentences(text);

    double index = 0.0588 * (count_letters(text) * 100 / (float) words) - 0.296 * (count_sentences(text) * 100 / (float) words) - 15.8;

    if (index >= 16)
    {
        printf("Grade 16+\n");
        return 0;
    }
    else if (index <= 1)
    {
        printf("Before Grade 1\n");
        return 0;
    }
    printf("Grade %.0f\n", round(index));
    return 0;
}


int count_letters(string text)
// counts number of letters in string
{
    int nletters = 0;

    // loops through all characters in string
    // if character is alphabetical, it counts a letter
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            nletters++;
        }
    }
    return nletters;
}


int count_words(string text)
// counts number of words in string
{
    int len = strlen(text);
    char prevchar;
    int nwords = 0;

    // if lenght of string is 0, there is no words
    if (len == 0)
    {
        return 0;
    }
    else
    {
        prevchar = text[0];
    }

    // loops through all characters in string
    // if encounters a space or \0, and previous
    // character is not a space, counts a word
    for (int i = 0; i < (len + 1) ; i++)
    {
        if ((isspace(text[i]) || text[i] == '\0') && prevchar != ' ')
        {
            nwords++;
        }
        prevchar = text[i];
    }
    return nwords;
}


int count_sentences(string text)
// counts all the sentences in a string
{
    int len = strlen(text);
    int nsentences = 0;

    // if lenght of string is 0, there is no sentences
    if (len == 0)
    {
        return 0;
    }

    // loops through all characters in string
    // if encounters a '.', '!' or '?' counts a sentence
    // if there is periods in other contexts
    // count is going to be incorect
    for (int i = 0; i < len; i++)
    {
        if ((text[i] == '.' || text[i] == '!' || text[i] == '?'))
        {
            nsentences++;
        }
    }
    return nsentences;
}