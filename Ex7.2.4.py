BOOM_NUM = 7


def seven_boom(end_number):
    """
    Builds a list of numbers between 0 to end_number where
    all multiples of 7 OR numbers that contain 7 are replaced with "BOOM"
    :param end_number: The max number to check
    :type end_number: int
    :return: The list with ints and "BOOM"s
    :rtype: list
    """
    final_list = []

    for i in range(end_number + 1):  # To include number itself
        if i % BOOM_NUM == 0 or i % 10 == BOOM_NUM:
            final_list.append("BOOM")
        else:
            final_list.append(i)

    return final_list


print(seven_boom(17))
