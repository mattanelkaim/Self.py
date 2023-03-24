# Get user input
current_guess = input("Guess a letter: ").lower()

if len(current_guess) != 1:
    if current_guess.isalpha():
        print("E1")  # Alphabetic but not 1 char
    else:
        print("E3")  # Not alphabetic & not 1 char
else:
    if current_guess.isalpha():
        print(current_guess)  # Valid guess
    else:
        print("E2")  # 1 char but not alphabetic
