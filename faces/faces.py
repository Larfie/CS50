"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

def convert(str_to_convert):
    new_str = ""
    # convert :) to emoji 🙂
    new_str = str_to_convert.replace(":)", "🙂")
    # convert :( to emoji 🙁
    new_str = new_str.replace(":(", "🙁")
    return new_str

def main():
    starting_str = input("Enter your input: ")
    print(convert(starting_str))

main()