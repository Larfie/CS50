from random import randint


def main():
    correct_counter = 0
    input_level = get_level()
    for i in range(0, 10):
        x = generate_integer(input_level)
        y = generate_integer(input_level)

        ans, i = None, 0

        while ans != x+y and i < 3:
            try:
                ans = int(input(f"{x} + {y} ="))
            except ValueError:
                i += 1
                print("EEE")
                continue
            i += 1
            if ans !=x+y:
                print("EEE")
        if i == 3:
            print(f"{x} + {y} = {x+y}")
        else:
            correct_counter += 1
    print(correct_counter)


def get_level():
    n = None
    while n not in [1,2,3]:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
    return n


def generate_integer(level):
    if level == 1:
        num = randint(0,9)
    else:
        num = randint(10**(level-1), (10**level) - 1)
    return num


if __name__ == "__main__":
    main()