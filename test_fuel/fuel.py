"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction):
    x, y = [num for num in fraction.split("/")]

    if x > y:
        raise ValueError
    elif not (x.isdigit() and y.isdigit()):
        raise ValueError
    elif  y == 0:
        raise ZeroDivisionError
    else:
        return (int(x)/int(y)) * 100


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
