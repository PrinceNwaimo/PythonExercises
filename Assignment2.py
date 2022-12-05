count = 0
number_to_be_guessed = 50
guess = int(input("Guess a number between 1 and 100: "))


while count < 3:
    if guess == number_to_be_guessed:
        print("Your guess is right", number_to_be_guessed,"Congratulations....",)
        break

    elif guess > number_to_be_guessed:
        print("Your guess is higher than the number,sorry ....")

    else:
        print("Your guess is lower than the number,sorry...")

    count += 3
