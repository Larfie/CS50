"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    random_font = choice(figlet.getFonts())
    figlet.setFont(font=random_font)
elif len(sys.argv) == 3 and sys.argv[1] in ["-f","--font"] and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Error: Incorrect arguments")

s = input()
print(figlet.renderText(s))