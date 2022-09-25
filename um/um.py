"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"\bum\b", s, flags=re.IGNORECASE))


if __name__ == "__main__":
    main()