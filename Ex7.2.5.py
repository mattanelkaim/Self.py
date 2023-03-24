def sequence_del(my_str):
    """
    Deletes identical letters in a row from a string
    :param my_str: The string to shorten
    :type my_str: str
    :return: The shortened string
    :rtype: str
    """
    if len(my_str) == 0:
        return ""  # Handle edge-case

    last_char = shortened_str = my_str[0]  # Init to first char
    for char in my_str:
        if char != last_char:
            shortened_str += char
            last_char = char  # Update last char to current000

    return shortened_str


print(sequence_del("Heeyyy   yyouuuu!!!"))

