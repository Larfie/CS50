from random import randint

n = 0
while n <= 0:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue


number = randint(0, n)

guess = None
while guess != number:
    try:
        guess = int(input("Type in your guess: "))
    except ValueError:
        continue
    
    if guess > number:
        print("Too large!")
    elif guess < number:
        print("Too small!")

print("Just right!")

