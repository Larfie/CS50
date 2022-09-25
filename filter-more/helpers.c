/* Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  */

#include "helpers.h"
#include <math.h>


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avr = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            avr = round((image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen) / 3.0);
            image[i][j].rgbtBlue = avr;
            image[i][j].rgbtRed = avr;
            image[i][j].rgbtGreen = avr;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, l = width / 2; j < l; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    int side = 1;

    // an array of RBGTRIPLE where we will store the new RGB values
    // we store in a temp so that the new value dont mess with the next pixels
    RGBTRIPLE temp_image[height][width];

    // loop through all pixel
    // we will sum each RBG value of each pixel in a 3x3 grid around the target pixel
    // (including this pixel), so we will end up with 3 sums: the sum of red, green and blue values
    // of all this pixels
    // Then we make the average for each RGB and store in the temp_image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float n_pixels = (2 * side + 1) * (2 * side + 1);
            int sumBlue = 0;
            int sumRed = 0;
            int sumGreen = 0;
            for (int r = -side; r <= side; r++)
            {
                for (int s = -side; s <= side; s++)
                {
                    // if in a edge or corner, there are pixel that dont exist,
                    // in this case we ignore them and remove 1 from this variable n_pixel
                    // which is the number of pixel to divide by during the mean calculation
                    if (i + r > height - 1 || i + r < 0 || j + s > width - 1 || j + s < 0)
                    {
                        n_pixels -= 1;
                        continue;
                    }
                    sumBlue += image[i + r][j + s].rgbtBlue;
                    sumRed += image[i + r][j + s].rgbtRed;
                    sumGreen += image[i + r][j + s].rgbtGreen;

                }
            }
            temp_image[i][j].rgbtBlue = round(sumBlue / n_pixels);
            temp_image[i][j].rgbtRed = round(sumRed / n_pixels);
            temp_image[i][j].rgbtGreen = round(sumGreen / n_pixels);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = temp_image[i][j].rgbtBlue;
            image[i][j].rgbtGreen = temp_image[i][j].rgbtGreen;
            image[i][j].rgbtRed = temp_image[i][j].rgbtRed;
        }
    }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    int side = 1;

    // sobel arrays
    // we will multiply each pixel around the current pixel by this values
    // depending on their position
    // for example the current pixel is in the middle so we multiply by 0
    // in both arrays
    int Gx[3][3] =
    {
        {-1, 0, 1},
        {-2, 0, 2},
        {-1, 0, 1}
    };
    int Gy[3][3] =
    {
        {-1, -2, -1},
        {0, 0, 0},
        {1, 2, 1}
    };

    // an array of RBGTRIPLE where we will store the new RGB values
    // we store in a temp so that the new value dont mess with the next pixels
    RGBTRIPLE temp_image[height][width];

    // loop through all pixels
    // for each pixel we will multiply by the sobel arrays
    // the RBG values of each pixel in a 3x3 array around the target pixel, including this pixel
    // then we will obtain 6 values, 2 for each RBG value, 1 for the x grid and 1 for grid y
    // once we have this values we can calculate the new RBG for that pixel
    // square root of gx^2 + gy^2
    // then we store the new RGB values in the temp_image array(we store in a temp so that the new value dont mess
    // with the next pixels)
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int temp_arr[3][2] = {{0}};
            for (int r = -side; r <= side; r++)
            {
                for (int s = -side; s <= side; s++)
                {
                    if (i + r > height - 1 || i + r < 0 || j + s > width - 1 || j + s < 0)
                    {
                        continue;
                    }
                    temp_arr[0][0] += image[i + r][j + s].rgbtRed * Gx[r + 1][s + 1];
                    temp_arr[0][1] += image[i + r][j + s].rgbtRed * Gy[r + 1][s + 1];
                    temp_arr[1][0] += image[i + r][j + s].rgbtGreen * Gx[r + 1][s + 1];
                    temp_arr[1][1] += image[i + r][j + s].rgbtGreen * Gy[r + 1][s + 1];
                    temp_arr[2][0] += image[i + r][j + s].rgbtBlue * Gx[r + 1][s + 1];
                    temp_arr[2][1] += image[i + r][j + s].rgbtBlue * Gy[r + 1][s + 1];

                }
            }
            int red = round(sqrt(temp_arr[0][0] * temp_arr[0][0] + temp_arr[0][1] * temp_arr[0][1]));
            int green = round(sqrt(temp_arr[1][0] * temp_arr[1][0] + temp_arr[1][1] * temp_arr[1][1]));
            int blue = round(sqrt(temp_arr[2][0] * temp_arr[2][0]  + temp_arr[2][1] * temp_arr[2][1]));

            temp_image[i][j].rgbtRed = (red > 255) ? 255 : red;
            temp_image[i][j].rgbtGreen = (green > 255) ? 255 : green;
            temp_image[i][j].rgbtBlue = (blue > 255) ? 255 : blue;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = temp_image[i][j].rgbtBlue;
            image[i][j].rgbtGreen = temp_image[i][j].rgbtGreen;
            image[i][j].rgbtRed = temp_image[i][j].rgbtRed;
        }
    }
    return;
}
