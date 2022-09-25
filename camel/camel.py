"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

camel_case = input("Enter the name of your variable in camelCase: ")

snake = ""
for character in camel_case:
    if character.isupper():
        snake += "_" + character.lower()
    else:
        snake += character

print(snake)


