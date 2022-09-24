import sys
import csv
from tabulate import tabulate


def main():
    check_arguments()

    try:
        file = csv.DictReader(open(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(file, headers="keys", tablefmt="grid" ))



def check_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()