import random
def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    number_to_guess = random.randint(1, 100) 
    attempts = 10 
    print("I have chosen a number between 1 and 100. Can you guess it?")
    print(f"You have {attempts} attempts.")
    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the correct number!")
            break
        attempts -= 1
        print(f"Attempts remaining: {attempts}")
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
guess_the_number()