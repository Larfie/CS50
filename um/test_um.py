"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

from um import count

def test_count_one():
    assert count("um?") == 1
    assert count("um ummi") == 1
    assert count("UM") == 1
    assert count("Um") == 1


def test_count_zero():
    assert count("ummm") == 0
    assert count("umumumum") == 0
    assert count("") == 0
    assert count("13") == 0

def test_count_more():
    assert count("Um um, UM") == 3
    assert count("#2 um! ola um, UM. no more ums") == 3
    
