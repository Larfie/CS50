/* Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  */

#include <stdio.h>
#include <ctype.h>
#include <string.h>

const unsigned int N = 186019;

unsigned int hash1(const char *word)
{
    // TODO: Improve this hash function
    unsigned long hash = (unsigned long) tolower(word[len - 1]);
    int p = 31;
    int len = strlen(word);
    //printf("%i\n", len);
    //printf("%s\n", word);

    for (int i = len - 1; i >= 0; i--)
    {
        char c = word[i];
        if (isupper(word[i]))
        {
            c = tolower(c);
        }
        hash = (hash * p + c) % N;
    }
    return hash;

}

unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned long hash = 5381;
    int i = 0;

    while (word[i] != '\0')
    {
        char c = word[i];
        hash = hash * 33 + c;
        i++;
    }
    return hash % N;
}

int main()
{
    char word[] = "fucko";
    printf("%i\n", hash1(word));
    return 0;
}