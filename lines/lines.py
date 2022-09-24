import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    try:
        if sys.argv[1].split(".")[-1] != "py":
            sys.exit("Not a Python file")
        file = open(sys.argv[1], "r")
    except (FileNotFoundError, ValueError):
        sys.exit("File does not exist")

    print(count_lines(file))

    file.close()


def count_lines(file):
    lines = file.readlines()

    count = 0
    for line in lines:
        if line.lstrip(" ")[0] == "#" or line.isspace():
            continue
        count += 1

    return count


if __name__ == "__main__":
    main()
