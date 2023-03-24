def count_chars(my_str):
    """
    Counts letters in a given string and saves results in a dict
    :param my_str: The string whose keys needs to be counted
    :type my_str: str
    :return: The results of the letters count, where the keys
             are the letters and values are their occurrences
    :rtype: dict
    """
    result = {}
    for letter in my_str:
        if letter == " ":  # Skip spaces
            continue

        if letter in result:  # If already exists
            result[letter] += 1
        else:
            result[letter] = 1  # Init letter in dict
    return result


magic_str = "Abra Cabrera"
print(count_chars(magic_str))
