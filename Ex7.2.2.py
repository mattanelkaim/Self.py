def numbers_letters_count(my_str):
    """
    Counts number of digits in a string
    :param my_str: The string to check
    :type my_str: str
    :return: A list, where first index is # of digits
             and second index is # of other characters
    :rtype: list
    """
    results = [0, 0]  # Digits & other chars
    for char in my_str:
        if char.isnumeric():
            results[0] += 1  # Inc

    results[1] = len(my_str) - results[0]  # Total chars - numeric chars = other chars
    return results


print(numbers_letters_count("Python 3.6.3"))
