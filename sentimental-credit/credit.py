from cs50 import get_int


def main():
    card = get_int("Number: ")

    sum = 0
    lenght = 0

    # Multiply every other digit by 2 then sums the results
    temp_number = card // 10
    while temp_number > 0:
        product = temp_number % 10 * 2
        while product > 0:
            sum += product % 10
            product //= 10
        temp_number //= 100
        lenght += 1

    # Add the previous sum to the sum of the digits that weren’t multiplied by 2
    temp_number = card
    while temp_number > 0:
        sum += temp_number % 10
        temp_number //= 100
        lenght += 1

    # Checks if last digit of the sum is 0 and the length of the card number is correct
    if sum % 10 == 0 and lenght >= 13 and lenght <= 16:
        temp_number = card

        # Loop to get the first and second digits
        while temp_number >= 100:
            temp_number //= 10
        second_digit = temp_number % 10
        first_digit = temp_number // 10

        # Checks card manufacter based on the first two digits
        if first_digit == 4 and lenght >= 13 and lenght <= 16:
            print("VISA")
        elif first_digit == 3 and lenght == 15 and (second_digit == 4 or second_digit == 7):
            print("AMEX")
        elif first_digit == 5 and lenght == 16 and (second_digit in [1, 2, 3, 4, 5]):
            print("MASTERCARD")
        else:
            print("INVALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
