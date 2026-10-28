import random

secret = random.randint(1, 20)
tries = 0
print("I'm thinking of a number between 1 and 20.")

while True:
    guess = int(input("Your guess: "))
    tries += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {tries} tries.")
        break