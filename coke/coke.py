print("Accepted coins: 25 cents, 10 cents, and 5 cents.")

total_sum = 0

while total_sum < 50:
    print(f"Amount due: {50-total_sum}")
    coin = int(input("Please enter a coin : "))
    if coin == 25 or coin == 10 or coin == 5:
        total_sum += coin
    else:
        print(f"Amount due: {50-total_sum}")

print(f"Change owed: {total_sum-50}")
