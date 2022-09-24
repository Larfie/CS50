
def main():
    print(shorten(input("Enter your string: ")))


def shorten(s):
    new_s = ""
    for c in s:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            new_s += c
    return new_s


if __name__ == "__main__":
    main()
