"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

from datetime import date
import inflect
import sys


def main():
    try:
        year, month, day = input("Date of birth: ").strip().split("-")
    except ValueError:
        sys.exit("Invalid Date format")

    print(convert_num_str(time_diff_minutes(int(year), int(month), int(day))).capitalize() + " minutes")


def convert_num_str(number):
    p = inflect.engine()
    return p.number_to_words(number, andword="")


def time_diff_minutes(i_year, i_month, i_day):
    today=date.today()
    return int(((today - date(i_year, i_month, i_day)).total_seconds()) / 60)


if __name__ == "__main__":
    main()