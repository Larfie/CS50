
def main():
    print(value(input("Input your greeting: ").lower().lstrip()))


def value(greeting):
    greeting = greeting.lower().lstrip()
    if greeting == "":
        return 100
    elif greeting[0:5] == "hello":
        return 0
    elif greeting[0] =="h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()