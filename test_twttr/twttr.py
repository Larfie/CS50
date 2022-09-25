"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""


def main():
    print(shorten(input("Enter your string: ")))


def shorten(s):
    new_s = ""
    for c in s:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            new_s += c
    return new_s


if __name__ == "__main__":
    main()
