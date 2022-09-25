"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

from random import randint

n = 0
while n <= 0:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue


number = randint(0, n)

guess = None
while guess != number:
    try:
        guess = int(input("Type in your guess: "))
    except ValueError:
        continue
    
    if guess > number:
        print("Too large!")
    elif guess < number:
        print("Too small!")

print("Just right!")

