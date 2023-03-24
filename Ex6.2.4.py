def extend_list_x(list_x, list_y):
    """
    Joins 2 lists into 1
    :param list_x: The parent list (to join to)
    :type list_x: list
    :param list_y: The children list (to join from)
    :type list_y: list
    :return: list_x (the joined list)
    :rtype: list
    """
    # list_x[:0] = list_y
    list_x[:0] = list_y
    return list_x


x = [4, 5, 6]
y = [1, 2, 3]
print(extend_list_x(x, y))
