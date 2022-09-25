"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

from seasons import convert_num_str, time_diff_minutes


def main():
    test_convert()
    test_time_diff()


def test_convert():
    assert convert_num_str(10) == "ten"
    assert convert_num_str(110) == "one hundred ten"


def test_time_diff():
    assert time_diff_minutes(2021, 7, 28) == 525600
    assert time_diff_minutes(2020, 7, 28) == 1051200


if __name__ == "__main__":
    main()