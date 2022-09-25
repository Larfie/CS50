"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""


def main():
    print(value(input("Input your greeting: ").lower().lstrip()))


def value(greeting):
    greeting = greeting.lower().lstrip()
    if greeting == "":
        return 100
    elif greeting[0:5] == "hello":
        return 0
    elif greeting[0] =="h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()