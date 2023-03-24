def longest(my_list):
    """
    Finds the longest element in a given list
    :param my_list: The list to search through
    :type: list (strings)
    :return: The longest string found
    :rtype: str
    """
    return sorted(my_list, key=len)[-1]


list1 = ["111", "234", "2000", "goru", "birthday", "09"]
print(longest(list1))
