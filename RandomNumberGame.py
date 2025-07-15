import random

secret_number = random.randint(1, 20)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 20: "))
    except ValueError:
        print("That's not a number. Try again...")
        continue

    attempts += 1

    if guess == secret_number:
        print("Nice! You got it! Digital High Five!")
        print(f"It only took you {attempts} guesses to get it!")
        play_again = input("Wanna go another round? (Yes/No): ").lower()
        if play_again == "yes":
            print("Alright, let's do this. Guess the number between 1 and 20.")
            secret_number = random.randint(1, 20)
            attempts = 0
            continue
        else:
            print("Cool beans. See you next time!")
            break
    elif guess < secret_number:
        print("Too low. Try again...")
    else:
        print("Nope, too high. Try again...")
