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
