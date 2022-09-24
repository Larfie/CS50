// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

int NODE_SIZE = sizeof(node);
unsigned long CHAR_SIZE = sizeof(char);

// TODO: Choose number of buckets in hash table
const unsigned int N = 186019; // terá de ser número primo e tem de ser 1.3 do numero de itens que vamos por

// Hash table
node *table[N];

int COUNT = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    unsigned int hash_value = (unsigned int) hash(word);
    node *temp = table[hash_value];
    if (temp == NULL)
    {
        return false;
    }
    while (temp != NULL)
    {
        if (strcasecmp(temp->word, word) == 0)
        {
            return true;
        }
        temp = temp->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int len = strlen(word);
    unsigned long hash = 0;
    int p = 31;
    //printf("%i\n", len);
    //printf("%s\n", word);

    for (int i = len - 1; i >= 0; i--)
    {
        char c = word[i];
        if (isupper(word[i]))
        {
            c = tolower(c);
        }
        hash = (hash * p + c);
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dfile = fopen(dictionary, "r");
    if (dfile == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        return false;
    }

    char buffer[LENGTH + 1];

    while (fscanf(dfile, "%s", buffer) == 1)
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            free(new_node);
            return false;
        }
        unsigned int hash_value = hash(buffer);
        strcpy(new_node->word, buffer);
        new_node->next = NULL;

        if (table[hash_value] == NULL)
        {
            table[hash_value] = new_node;
            // printf("%s\n", table[hash_value]->word);
        }
        else
        {
            new_node -> next = table[hash_value];
            table[hash_value] = new_node;
            // printf("%s\n", table[hash_value]->word);
        }
        COUNT++;

    }
    //for (int i = 0; i < N; i++)
    //{
    p//printf("%s\n", table[i]->word);
    //}
    fclose(dfile);
    return true;

}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return COUNT;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
        while (table[i] != NULL)
        {
            node *tmp = table[i]->next;
            free(table[i]);
            table[i] = tmp;
        }
    return true;
}
