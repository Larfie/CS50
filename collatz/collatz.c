/* Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  */

#include <stdio.h>
#include <cs50.h>

int collatz(int n);

int main(void)
{
    int num = get_int("Number: ");
    printf("%i\n", collatz(num));
}

int collatz(int n)
{
    if (n == 1)
    {
        return 0;
    }
    else if (n % 2 == 0)
    {
        return 1 + collatz(n/2);
    }
    else
    {
        return 1 + collatz(3 * n + 1);
    }
}