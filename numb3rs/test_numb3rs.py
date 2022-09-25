"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

from numb3rs import validate


def main():
    test_validate1()
    test_validate2()


def test_validate1():
    assert validate("255.255.255.255") == True
    assert validate ("0.0.0.0") == True
    assert validate("1.25.135.0") == True


def test_validate2():
    assert validate("cat") == False
    assert validate("255.255.255.!10") == False
    assert validate ("255.255.255") == False
    assert validate("0.0.0.0.0.0.0") == False
    assert validate("1.2.3.1000") == False
    assert validate(" ") == False
    assert validate("1.(.(.1000") == False
    assert validate("75.456.76.65") == False


if __name__ == "__main__":
    main()