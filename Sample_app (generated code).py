import random

def play():
    secret_number = random.randint(1, 100)
    points = 100

    while True:
        print("You have", points, "points.")
        guess = int(input("Guess the number between 1 and 100 (or type -1 to quit): "))

        if guess == -1:
            break
        elif guess < secret_number:
            print("too low")
            points -= 1
        elif guess > secret_number:
            print("too high")
            points -= 1
        else:
            print("You win with", points, "points remaining.")
            break

    if points > 0:
        print("Game over. The number was", secret_number)

play()