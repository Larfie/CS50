"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

# TODO
from cs50 import get_int


def main():
    # Asks input for height of pyramid until we get a value between 1-8
    height = get_int("Height: ")
    while (height < 1 or height > 8):
        height = get_int("Height: ")

    # Loop each row of the pyramid
    for i in range(1, height + 1):
        lead_spaces = height - i
        print(" " * lead_spaces, end="")
        print("#" * i, end="")
        print(" " * 2, end="")
        print("#" * i)


if __name__ == "__main__":
    main()
