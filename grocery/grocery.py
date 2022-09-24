def main():
    grocery_dict = get_items()
    for key in sorted(grocery_dict.keys()):
        print(grocery_dict[key], key, sep=" ")

def get_items():
    d = {}

    while True:
        try:
            item = input().upper()
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        except EOFError:
            print("\n")
            return d


main()