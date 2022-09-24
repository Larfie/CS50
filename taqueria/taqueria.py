dict_taqueria = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def get_items():
    total = 0
    while True:
        try:
            total += dict_taqueria[input("Item: ").title()]
        except EOFError:
            print("\n")
            break
        except KeyError:
            pass
        else:
            print("Total: ${:,.2f}".format(total))


get_items()