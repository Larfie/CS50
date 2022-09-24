// asks for height and then prints pyramid with that height
#include <cs50.h>
#include <stdio.h>

int main(void)
// print x spaces (where x = height - iteration) then print "#" iteration times then 2 spaces then "#" iteration times
{
    // asks input until input is in 1-8 range
    int height = get_int("Height: ");
    while (height < 1 || height > 8)
    {
        height = get_int("Height: ");
    }

    int iter = 1;
    do
    {
        int n = height - iter;
        int x;
        for (x = 0; x < n; x++)
        {
            printf(" ");
        }

        for (x = 0; x < iter; x++)
        {
            printf("#");
        }

        printf("  ");

        for (x = 0; x < iter; x++)
        {
            printf("#");
        }
        printf("\n");
        iter++;
    }
    while (iter <= height);
}

