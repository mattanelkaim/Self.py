def sort_anagrams(list_of_strings):
    """
    Sorts strings into lists of anagrams (identical letters)
    :param list_of_strings: The list of strings to sort to anagrams
    :type list_of_strings: list
    :return: A list of lists of anagrams
    :rtype: list
    """

    result = []
    for word in list_of_strings:
        flag = True  # Not found
        for group in result:
            if sorted(word) == sorted(group[0]):
                for option in result:
                    if sorted(word) == sorted(option[0]):
                        option.append(word)
                        flag = False  # Appended successful
        if flag:  # Not appended
            result.append([word])
    return result


list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
print(sort_anagrams(list_of_words))
