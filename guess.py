import random
number_to_be_guessed = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

count = 0
while count < 2:

    if guess == number_to_be_guessed:
        print("You got it right")
        break

    else:
        guess = int(input("Guess a number between 1 and 100: "))

    count += 1

    if count == 2:
        print("Try again later,its unfortunate you could not guess", number_to_be_guessed)
