"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

x, y , z = input("Enter your arithmetic expression:  ").split()
x, z = int(x), int(z)

if y == "+":
    print("{:.1f}".format(x+z))
elif y == "-":
    print("{:.1f}".format(x-z))
elif y == "/":
    print("{:.1f}".format(x/z))
elif y == "*":
    print("{:.1f}".format(x*z))
