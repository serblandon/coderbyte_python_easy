import random

#nb = random.random()
nb = 7

x = int(input("Guess the number: "))

while x != nb:
    x = int(input("Try again: "))

print(f"The number is {nb}")