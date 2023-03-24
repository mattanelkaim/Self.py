def squared_numbers(start, stop):
    """
    Calculates powers of 2 between start and stop
    :param start: The number to start from
    :type start: int
    :param stop: The number to stop
    :type stop: int
    :return: A list of calculated powers of 2
    :rtype: list
    """
    # Calculating and appending all powers of 2
    return [num ** 2 for num in range(start, stop + 1)]  # Include stop


print(squared_numbers(1, 3))
