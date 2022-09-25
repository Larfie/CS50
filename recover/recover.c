/* Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

// Size of each block
int BLOCK_SIZE = 512;

// Creates a BYTE type of data
typedef uint8_t BYTE;


int main(int argc, char *argv[])
{
    // Checks if there is exactly 1 argument (name of file is 0, so we have to check for 2)
    if (argc != 2)
    {
        printf("Wrong usage!\nUsage: ./recover IMAGE\n");
        return 1;
    }

    //
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fclose(file);
        printf("Could not open %s.\n", argv[1]);
        return 2;
    }


    BYTE *buffer = malloc(BLOCK_SIZE);
    int counter = 0;
    bool flag_first = true;
    char filename[8];
    sprintf(filename, "%03i.jpg", counter);
    FILE *image = fopen(filename, "w");
    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xff) == 0xe0)
        {
            if (flag_first == true)
            {
                fwrite(buffer, 1, BLOCK_SIZE, image);
                flag_first = false;
            }
            else
            {
                fclose(image);
                counter++;
                sprintf(filename, "%03i.jpg", counter);
                image = fopen(filename, "w");
                fwrite(buffer, 1, BLOCK_SIZE, image);
            }
        }
        else if (flag_first == false)
        {
            fwrite(buffer, 1, BLOCK_SIZE, image);
        }
    }
    fclose(image);
    free(buffer);
    fclose(file);
}