def shift_left(my_list):
    """
    Shifts all elements in a 3-element list to the left
    :param my_list: The list to shift to left
    :type my_list: list
    :return: The shifted list (to left)
    :rtype: list
    """
    # WE DON'T NEED A TEMPORARY VARIABLE!!
    my_list[0], my_list[1], my_list[2] = my_list[1], my_list[2], my_list[0]
    return my_list


print(shift_left(['monkey', 2.0, 1]))
