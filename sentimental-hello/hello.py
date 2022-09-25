"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

from cs50 import get_string


# Main function
# Asks name and then prints hello, "name"
def main():
    name = get_string("What is your name? ")
    print(f"Hello, {name}")


if __name__ == "__main__":
    main()
