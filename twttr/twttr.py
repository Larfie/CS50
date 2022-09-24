text = input("Enter your string: ")

new_text = ""
for c in text:
    if c.lower() not in ["a", "e", "i", "o", "u"]:
        new_text += c

print(new_text)