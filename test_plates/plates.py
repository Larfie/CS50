"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[0:2].isalpha():
        return False

    digit = False
    for char in s:
        if char.isalpha() and digit == False:
            continue
        elif char.isdigit() and digit == False:
            if char == "0":
                return False
            else:
                digit = True
        elif char.isdigit() and digit == True:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    main()