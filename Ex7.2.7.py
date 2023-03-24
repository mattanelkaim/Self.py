def arrow(my_char, max_length):
    """
    Builds an arrow made of 'my_char', ascends to max_length then descends to 0
    :param my_char: The char that builds the arrow
    :type my_char: str
    :param max_length: Length of middle row, which is max
    :type max_length: int
    :return: The arrow made of my_char
    :rtype: str
    """
    if max_length <= 0:  # Edge-case
        return ""  # Invalid length

    my_str = my_char  # First
    for i in range(2, max_length + 1):
        my_str += "\n" + my_char * i
    for i in range(max_length - 1, 0, -1):
        my_str += "\n" + my_char * i
    return my_str


print(arrow('*', 5))
