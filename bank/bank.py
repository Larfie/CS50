"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

greeting = input("Input your greeting: ").lower().lstrip()

if greeting[0:5] == "hello":
    print("$0")
elif greeting[0] =="h":
    print("$20")
else:
    print("$100")