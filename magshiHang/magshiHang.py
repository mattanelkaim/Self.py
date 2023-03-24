from os.path import exists  # To check words file

MAX_TRIES = 6
HANGMAN_ASCII_ART = """\
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                          __/ |                      
                         |___/"""
HANGMAN_PHOTOS = {
        0: "    x-------x",
        1: """\
    x-------x
    |
    |
    |       
    |
    |""",
        2: """\
    x-------x
    |       |
    |       0
    |       
    |
    |""",
        3: """\
    x-------x
    |       |
    |       0
    |       |
    |
    |""",
        4: """\
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
        5: """\
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",
        6: """\
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""
}


def print_welcome_message():
    """
    Prints an ASCII-art welcome message XD
    :return: None
    """
    print(HANGMAN_ASCII_ART)


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Returns whether guess is valid or not:
    Only 1 character, only alphabetic, didn't guess this before
    :param old_letters_guessed: A list of old valid guesses
    :type old_letters_guessed: list
    :param letter_guessed: user's guess to check
    :type letter_guessed: str
    :return: Whether guess is valid or not (True/False)
    :rtype: boolean
    """

    return len(letter_guessed) == 1 and letter_guessed.isalpha() \
        and letter_guessed.lower() not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Appends new guess to old guesses if guess is valid,
    Else prints the guessed letters
    :param letter_guessed: The current guess of the user
    :type letter_guessed: str
    :param old_letters_guessed: A list of the old guesses
    :type old_letters_guessed: list
    :return: Whether append was successful or not
    :rtype: boolean
    """

    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    # Else, invalid guess
    print("X")
    if len(old_letters_guessed) != 0:
        print("Old letters: ", end="")
        print(" -> ".join(sorted(old_letters_guessed)))
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    Builds a hidden string (based on secret_word) where
    all letters in old_letters_guessed are revealed
    :param secret_word: The hidden word
    :type secret_word: str
    :param old_letters_guessed: All the previous valid guesses
    :type old_letters_guessed: list
    :return: A string in which correct guesses are revealed
    :rtype: str
    """
    revealed = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            revealed.append(letter)
        else:
            revealed.append("_")
    return " ".join(revealed)


def check_win(secret_word, old_letters_guessed):
    """
    Checks whether user has guesses all letters in secret_word
    :param secret_word: The word to guess
    :type secret_word: str
    :param old_letters_guessed: All the previous valid guesses
    :type old_letters_guessed: list
    :return: Whether user has won or not
    :rtype: boolean
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False  # User didn't guess all letters
    return True  # User guessed all letters


def print_hangman(num_of_tries):
    """
    Prints the current state of the hangman
    :param num_of_tries: The state of the hangman
    :type num_of_tries: int
    :return: None
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def choose_word(file_path, index):
    """
    Reads a file with words separated by spaces, 1 line.
    Finds the word in the file in the (index)th spot.
    :param file_path: The path to the words file
    :type file_path: str
    :param index: The index (from 1) of the word
    :type index: int
    :return: Word at specified index
    :rtype: str
    """
    # "Index" from user actually starts from 1, not from 0
    index -= 1  # Normalize to index
    with open(file_path, 'r') as file:
        content = file.read().split()

    return content[index % len(content)]  # Counts index back from zero if out of boundaries


def main():
    # INITIALIZE
    print_welcome_message()

    num_of_tries = 0  # Failed tries
    old_letters_guessed = []
    has_won = False
    print("You have", MAX_TRIES, "guesses\n")

    # INIT SECRET WORD
    while True:  # Get a valid path for the file
        file_path = input("Enter words file path: ")
        if exists(file_path):
            break
        print("No file found at \"", {file_path}, "\"! Try again")  # Else, path is invalid!
    secret_word_index = int(input("Enter the index of the word: "))
    secret_word = choose_word(file_path, secret_word_index).lower()

    print("\nYour hangman: ")
    print_hangman(num_of_tries)
    print()  # New line

    # GAME LOOP
    while not has_won:  # Break when won/lost
        print(show_hidden_word(secret_word, old_letters_guessed))

        # GET USER INPUT
        current_guess = input("Guess a letter: ").lower()

        # Check guess validity and update old_letters_guessed if valid
        is_guess_valid = try_update_letter_guessed(current_guess, old_letters_guessed)

        has_won = check_win(secret_word, old_letters_guessed)

        # Check for a wrong guess: valid guess AND guess is wrong AND not won
        if is_guess_valid and current_guess not in secret_word:
            print(":(")
            num_of_tries += 1  # Increase
            print_hangman(num_of_tries)
            if num_of_tries == MAX_TRIES:
                break  # Break from game loop, game ended!
            print(MAX_TRIES - num_of_tries, "tries left!")  # Else, continue the game
        print()  # New line

    # Game ended
    print(show_hidden_word(secret_word, old_letters_guessed))  # Show final word
    if has_won:
        print("WIN")  # Won
    else:
        print("LOSE")  # Lost


if __name__ == '__main__':
    main()
