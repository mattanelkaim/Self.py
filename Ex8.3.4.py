def inverse_dict(my_dict):
    """
    Inverts a key of a dict into sorted lists of values, and values into keys. Turns these into a new dict
    :param my_dict: The dictionary to inverse
    :type my_dict: dict
    :return: The inverted dict (inverted the original)
    :rtype: dict
    """
    result = {}
    for key, value in my_dict.items():  # Invert keys and values
        result.setdefault(value, []).append(key)
    for value in result:  # Then sort each element
        result[value].sort()
    return result


course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))
