import random

def guess (x):
    correct_guess = random.randint (1,x)
    user_guess = 0
    while user_guess != correct_guess:
        user_guess = int(input(f"Guess a number between 1 and {x}!: "))
        if user_guess < correct_guess:
            print("Too low. Try again.")
        if user_guess > correct_guess:
            print("Too high. Try again.")
    print("Correct!")
guess (50)

