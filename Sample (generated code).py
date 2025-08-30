import random
secretNumber = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")

# initialize variables
guessesTaken = 0
points = 100

# keep looping until user guesses correctly or runs out of points
while points > 0 and not guessesTaken > secretNumber:

    # ask user to guess
    guess = int(input("Take a guess: "))

    # give a clue
    if guess > secretNumber:
        print("Your guess is too high.")
    elif guess < secretNumber:
        print("Your guess is too low.")

    # deduct a point
    points = points - 1

# reveal answer
print("The secret number was " + str(secretNumber))

# if the user ran out of points, tell them they lost
if points == 0:
    print("Sorry, you ran out of guesses. You lose.")

# if the user guessed correctly, tell them they won
else:
    print("Good job! You won!")