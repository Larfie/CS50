"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

import inflect

def main():
    names = get_names()

    p = inflect.engine()

    print("Adieu, adieu, to ", end="")
    print(p.join(names))



def get_names():
    list_names = []

    while True:
        try:
            list_names.append(input("Name: "))
        except EOFError:
            print()
            return list_names

main()