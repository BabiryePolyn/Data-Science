correct_number = 7
guess = 0

print("Guess a number between 1 and 10!")

while guess != correct_number:
    guess = int(input("Enter your guess: "))
    
    if guess != correct_number:
        print("Wrong! Try again.")
    else:
        print("Correct! You guessed it!")

print("Game over!")