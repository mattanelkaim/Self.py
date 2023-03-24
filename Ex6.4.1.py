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
