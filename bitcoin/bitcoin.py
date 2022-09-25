"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit("Wrong arguments")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Not a float")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit()

rate = response.json()["bpi"]["USD"]["rate_float"]
cost = rate * n

print(f'${cost:,}')