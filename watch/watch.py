"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if capture := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})"', s):
        return f"https://youtu.be/{capture.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()