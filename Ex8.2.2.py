def sort_prices(list_of_tuples):
    """
    Sorts a list of tuples in descending order
    by the second element of each tuple
    :param list_of_tuples: The list to sort
    :type list_of_tuples: list
    :return: The sorted list of tuples
    :rtype: list
    """
    # - in lambda to sort in descending order, key is second element in each tuple
    return sorted(list_of_tuples, key=lambda element: -float(element[1]))
