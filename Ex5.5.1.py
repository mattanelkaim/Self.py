def is_valid_input(letter_guessed):
    """
    Returns whether guess is valid or not:
    Only 1 character, only alphabetic
    :param letter_guessed: user's guess to check
    :type letter_guessed: str
    :return: Whether guess is valid or not (True/False)
    :rtype: boolean
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha()
