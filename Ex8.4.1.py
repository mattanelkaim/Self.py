def print_hangman(num_of_tries):
    """
    Prints the current state of the hangman
    :param num_of_tries: The state of the hangman
    :type num_of_tries: int
    :return: None
    """
    HANGMAN_PHOTOS = {
        1: "    x-------x",
        2: """\
    x-------x
    |
    |
    |       
    |
    |""",
        3: """\
    x-------x
    |       |
    |       0
    |       
    |
    |""",
        4: """\
    x-------x
    |       |
    |       0
    |       |
    |
    |""",
        5: """\
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
        6: """\
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",
        7: """\
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""
    }
    print(HANGMAN_PHOTOS[num_of_tries])


print_hangman(1)
