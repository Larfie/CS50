"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

text = input("Enter your string: ")

new_text = ""
for c in text:
    if c.lower() not in ["a", "e", "i", "o", "u"]:
        new_text += c

print(new_text)