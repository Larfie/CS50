#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>


string cypher(string s, string key);


int main(int argc, string argv[])
{
    if (argc != 2 || strlen(argv[1]) != 26)
    {
        printf("Wrong arguments!\n");
        return 1;
    }

    // Converts key string to uppercase
    // validates key, by checking if contains
    // non-alpha characters or duplicates
    string key = argv[1];
    int len = strlen(argv[1]);
    for (int i = 0; i < len; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Invalid characters in key!\n");
            return 1;
        }
        key[i] = toupper(key[i]);
        for (int f = i + 1; f < len - 1; f++)
        {
            if (key[i] == toupper(key[f]))
            {
                printf("Duplicate characters in key!\n");
                return 1;
            }
        }
    }

    string text = get_string("plaintext: ");

    string result = cypher(text, key);

    printf("ciphertext: %s\n", result);

    return 0;
}


string cypher(const string s, string key)
// Loop through each chracter in string s,
// and subtract 65 from ascii value, so that we can
// then substitute that character by key[subtraction result]
// which will be the equivalent in the key string
// if character in string s is lowercase, we lowercase it in the
// returned string
{
    int flag;
    const int len = strlen(s);

    for (int i = 0; i < len; i++, flag = 0)
    {
        if (isalpha(s[i]))
        {
            if (islower(s[i]))
            {
                flag = 1;
            }
            s[i] = toupper(s[i]);
            s[i] = key[s[i] - 65];
            if (flag)
            {
                s[i] = tolower(s[i]);
            }
        }

    }
    return s;
}