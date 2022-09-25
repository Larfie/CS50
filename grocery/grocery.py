"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

def main():
    grocery_dict = get_items()
    for key in sorted(grocery_dict.keys()):
        print(grocery_dict[key], key, sep=" ")

def get_items():
    d = {}

    while True:
        try:
            item = input().upper()
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        except EOFError:
            print("\n")
            return d


main()