import inflect

def main():
    names = get_names()

    p = inflect.engine()

    print("Adieu, adieu, to ", end="")
    print(p.join(names))



def get_names():
    list_names = []

    while True:
        try:
            list_names.append(input("Name: "))
        except EOFError:
            print()
            return list_names

main()