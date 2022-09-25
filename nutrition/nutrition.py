"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

fruits = {"Apple": 130, "Avocado": 50, "Banana": 110, "Cantaloupe": 50, "Grapefruit": 60, "Grapes": 90, "Honeydew Melon": 50, "Kiwifruit": 90, "Lemon": 15, "Lime":20 , "Nectarine": 60, "Orange": 80, "Peach": 60, "Pear":100 , "Pineapple": 50, "Plums": 70, "Strawberries": 50, "Sweet Cherries":100, "Tangerine": 50, "Watermelon": 80}

def main():
    user_fruit = input("Fruit: ").title()
    if user_fruit in fruits:
        print(fruits[user_fruit])

main()
