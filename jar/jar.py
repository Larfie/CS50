"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("The capacity of the jar was exceeded")

        print(f"{n} cookies were added to the jar")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies in the jar")

        print(f"{n} cookies were removed from the jar")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Non-positive number of cookies")
        self._capacity = value


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
