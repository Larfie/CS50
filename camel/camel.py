camel_case = input("Enter the name of your variable in camelCase: ")

snake = ""
for character in camel_case:
    if character.isupper():
        snake += "_" + character.lower()
    else:
        snake += character

print(snake)


