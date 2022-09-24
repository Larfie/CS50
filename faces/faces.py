def convert(str_to_convert):
    new_str = ""
    # convert :) to emoji 🙂
    new_str = str_to_convert.replace(":)", "🙂")
    # convert :( to emoji 🙁
    new_str = new_str.replace(":(", "🙁")
    return new_str

def main():
    starting_str = input("Enter your input: ")
    print(convert(starting_str))

main()