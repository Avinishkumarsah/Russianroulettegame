import random
num = random.randint(1,10)
guess = input("Guess a number between 1 to 10")
guess = int(guess)
if guess == num:
    print("You Won!")
else:
    print("You lose!")
