"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

from validator_collection import checkers


def main():
    print(email_validation(input("What's your email adress? ")))


def email_validation(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()