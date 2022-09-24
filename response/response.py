from validator_collection import checkers


def main():
    print(email_validation(input("What's your email adress? ")))


def email_validation(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()