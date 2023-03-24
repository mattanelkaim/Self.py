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
        print(" -> ".join(sorted(old_letters_guessed)))
    return False
