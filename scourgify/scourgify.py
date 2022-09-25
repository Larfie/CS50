"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

import sys
import csv
import os.path


def main():
    check_arguments(2, ".csv")

    if not os.path.exists(sys.argv[1]):
        sys.exit(f"Could not read {sys.argv[1]}")

    dict_corrected = separate_names(sys.argv[1])

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in dict_corrected:
            writer.writerow(dict_corrected[row])


def separate_names(file_location):
    dict_all_names_and_house = {}

    with open(file_location, "r") as file:
        reader = csv.reader(file)
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
                continue
            last_name, first_name = row[0].split(", ")
            house = row[1]
            dict_all_names_and_house[line_count] = {"first": first_name, "last": last_name, "house": house}
            line_count += 1

    return dict_all_names_and_house


def check_arguments(num_arguments, file_types):
    # Função para verificar se foram passados o numero correto de argumenos e se o tipo de ficheiro é o correto
    if len(sys.argv) < num_arguments + 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > num_arguments + 1:
        sys.exit("Too many command-line arguments")

    for num in range(1, num_arguments + 1):
        if not any(type in sys.argv[num].lower() for type in file_types):
            sys.exit("Not a valid file")


if __name__ == "__main__":
    main()