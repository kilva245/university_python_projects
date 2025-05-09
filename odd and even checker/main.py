
odds = ""
evens = ""

for i in range(10):
    number = int(input(f"Enter your number {i + 1} : "))
    if number % 2 == 0:
        evens = evens + str(number) + " "
    else:
        odds = odds + str(number) + " "

print("\neven numbers: ", evens)
print("odd numbers: ", odds)