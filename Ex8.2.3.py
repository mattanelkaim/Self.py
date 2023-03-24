def mult_tuple(tuple1, tuple2):
    """
    Builds a big tuple with all possible combinations
    between all the elements from tuple1 and tuple2
    :param tuple1: The first tuple to build combinations from
    :type tuple1: tuple
    :param tuple2: The second tuple to build combinations from
    :type tuple2: tuple
    :return: The big tuple with all possible combinations
    :rtype: tuple
    """
    list_of_tuples = []
    for i in tuple1:
        for j in tuple2:
            list_of_tuples.append((i, j))
            list_of_tuples.append((j, i))
    return tuple(list_of_tuples)


first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
print(mult_tuple(first_tuple, second_tuple))
