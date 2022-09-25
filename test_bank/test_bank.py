"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

from bank import value


def main():
    test_value_start_hello()
    test_value_start_h()
    test_value_nothing()


def test_value_start_hello():
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello,") == 0
    assert value("Hello, agent 47") == 0


def test_value_start_h():
    assert value("h") == 20
    assert value("H") == 20
    assert value("h") == 20
    assert value("H,47") == 20


def test_value_nothing():
    assert value("son of a ...") == 100
    assert value("idiot") == 100
    # assert value("   ") == 100
    assert value("47") == 100
    assert value("Not hello") == 100


if __name__ == "__main__":
    main()
