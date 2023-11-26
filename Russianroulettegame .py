import random
num = random.randint(1,100)
guess = input("Guess a number between 1 to 100")
guess = int(guess)
if guess == num:
    print("You Won!")
else:
    print("You lose!")
