def choose_word(file_path, index):
    """
    Reads a file with words separated by spaces, 1 line.
    Finds number of unique words, the word in the file in the (index)th spot
    :param file_path: The path to the words file
    :type file_path: str
    :param index: The index (from 1) of the word
    :type index: int
    :return: Word at specified index
    :rtype: tuple: int, str
    """
    # "Index" from user actually starts from 1, not from 0
    index -= 1  # Normalize to index
    with open(file_path, 'r') as file:
        content = file.read().split()
    no_duplicates = set(content)

    return len(no_duplicates), content[index % len(content)]  # Counts index back from zero if out of boundaries
