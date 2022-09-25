"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

from twttr import shorten

def main():
    test_shorten()


def test_shorten1():
    assert shorten("twitter") == "twttr"


def test_shorten2():
    assert shorten("45rtTa") == "45rtT"


def test_shorten3():
    assert shorten("...") == "..."

def test_shorten4():
    assert shorten("AeIoU RRRd") == " RRRd"


if __name__ == "__main__":
    main()
