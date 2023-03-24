def format_list(my_list):
    """
    Turns a list into a string of the even elements + last element
    :param my_list: The list to format
    :type my_list: list
    :return: The formatted string
    :rtype: str
    """
    formatted_str = ", ".join(my_list[::2]) + ", and " + my_list[-1]
    return formatted_str


elements = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print(format_list(elements))
