"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

import csv
import sys
import re


def main():

    # Check for command-line usage
    check_arguments(2)

    # Read database file in to a variable
    dna_db = []
    with open(sys.argv[1], "r") as db_file:
        reader = csv.DictReader(db_file)
        str_list = reader.fieldnames
        for entry in reader:
            dna_db.append(entry)
    str_list.remove("name")

    # Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as seq_file:
        sequence = seq_file.read()

    # Find longest match of each STR in DNA sequence
    str_count = {}
    for substring in str_list:
        temp_list = re.findall(f"(?:{substring})+", sequence)
        longest_match = 0
        for i in temp_list:
            if len(i) > longest_match:
                longest_match = len(i)
        longest_match /= len(substring)
        str_count[substring] = longest_match

    # TODO: Check database for matching profiles
    matches = set()
    for db in dna_db:
        str_length = len(str_count)  # how many str we have to check
        for key in str_count:
            str_length -= 1
            if str_count[key] != int(db[key]):
                break
            elif str_length == 0:
                matches.add(db["name"])
            else:
                continue

    if matches:
        for match in matches:
            print(match)
    else:
        print("No match")
    return


def check_arguments(num_arguments):
    # Função para verificar se foram passados o numero correto de argumentos
    if len(sys.argv) < num_arguments + 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > num_arguments + 1:
        sys.exit("Too many command-line arguments")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
