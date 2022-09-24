x, y , z = input("Enter your arithmetic expression:  ").split()
x, z = int(x), int(z)

if y == "+":
    print("{:.1f}".format(x+z))
elif y == "-":
    print("{:.1f}".format(x-z))
elif y == "/":
    print("{:.1f}".format(x/z))
elif y == "*":
    print("{:.1f}".format(x*z))
