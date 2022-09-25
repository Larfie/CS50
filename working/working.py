"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"([0-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)", s)

    if matches:
        parts = matches.groups()
        if int(parts[0]) > 12 or int(parts[3]) > 12:
            raise ValueError
        else:
            first_hour = format_change_12_to_24(parts[0], parts[1], parts[2])
            second_hour = format_change_12_to_24(parts[3], parts[4], parts[5])

            return f"{first_hour} to {second_hour}"


    else:
        raise ValueError


def format_change_12_to_24(hours, minutes, am_pm):
    if minutes == None:
        minutes = 0
    if am_pm == "AM":
        if int(hours) == 12:
            return f"{00:02d}:{int(minutes):02d}"
        return f"{int(hours):02d}:{int(minutes):02d}"
    elif am_pm == "PM":
        if int(hours) == 12:
            return f"{12:02d}:{int(minutes):02d}"
        return f"{int(hours)+12:02d}:{int(minutes):02d}"


if __name__ == "__main__":
    main()