"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

if answer == "42" or answer == "forty two" or answer == "forty-two":
    print("Yes")
else:
    print("No")