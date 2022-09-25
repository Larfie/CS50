"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

from emoji import emojize

def main():
    emoji_code = input("Type in your emoji code: ")
    print(emojize(emoji_code))

main()