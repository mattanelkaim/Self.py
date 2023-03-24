def are_lists_equal(list1, list2):
    """
    Checks whether 2 given lists have the same elements
    :param list1: First list to compare
    :type list1: list
    :param list2: Second list to compare
    :type list2: list
    :return: Whether lists are equal or not
    :rtype: boolean
    """
    return sorted(list1) == sorted(list2)


list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]

print(are_lists_equal(list1, list2))
