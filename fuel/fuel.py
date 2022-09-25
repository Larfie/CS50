"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

def main():
    fract = get_fraction()
    if fract >= 0.99:
        print("F")
    elif fract <= 0.01:
        print("E")
    else:
        print("{0:.0%}".format(fract))


def get_fraction():
    while True:
        try:
            x, y = [int(num) for num in input("What's X/Y? ").split("/")]
        except ValueError:
            pass
        else:
            if y == 0 or x > y:
                continue
            else:
                return x/y

main()


