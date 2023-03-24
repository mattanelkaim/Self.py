def is_greater(my_list, n):
    """
    Removes elements smaller than n from the given list
    :param my_list: The list to check
    :type my_list: list
    :param n: Number to compare to
    :type n: int
    :return: The list with the elements bigger than n
    :rtype: list
    """
    return [x for x in my_list if x > n]


print(is_greater([1, 30, 25, 60, 27, 28], 28))
