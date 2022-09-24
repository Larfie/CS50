from cs50 import get_string


# Main function
# Asks name and then prints hello, "name"
def main():
    name = get_string("What is your name? ")
    print(f"Hello, {name}")


if __name__ == "__main__":
    main()
