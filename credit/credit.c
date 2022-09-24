// checks the validity of a credit card number

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // gets credit card number from user
    const long NUMBER = get_long("Number: ");

    int sum = 0;
    int fdigit;
    int sdigit;
    int lenght = 0;

    // Multiply every other digit by 2 then sums the results
    long copynumber = NUMBER / 10;
    int product;
    while (copynumber > 0)
    {
        product = (copynumber % 10) * 2;
        while (product > 0)
        {
            sum += product % 10;
            product /= 10;
        }
        copynumber /= 100;
        lenght++;

    }

    // Add the previous sum to the sum of the digits that weren’t multiplied by 2
    copynumber = NUMBER;
    while (copynumber > 0)
    {
        sum += copynumber % 10;
        copynumber /= 100;
        lenght++;
    }

    // If the total’s last digit is 0 the number is valid
    if (sum % 10 == 0 && lenght >= 13 && lenght <= 16)
        // gets the first and second digit of credit card number to check the card's maker
        // also checks lenght of number
    {
        copynumber = NUMBER;
        while (copynumber >= 100)
        {
            copynumber /= 10;
        }
        sdigit = copynumber % 10;
        fdigit = copynumber / 10;

        if (fdigit == 4 && lenght >= 13 && lenght <= 16)
        {
            printf("VISA\n");
        }
        else if (fdigit == 3 && lenght == 15 && (sdigit == 4 || sdigit == 7))
        {
            printf("AMEX\n");
        }
        else if (fdigit == 5 && lenght == 16 && (sdigit == 1 || sdigit == 2 || sdigit == 3 || sdigit == 4 || sdigit == 5))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}


