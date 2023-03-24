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
