MAX_ITEM_LEN = 3


def main():
    groceries = input("Please enter your groceries: ").split(",")
    print("""1 - Print groceries list\
           \n2 - Print # of groceries\
           \n3 - Find an item in list\
           \n4 - Count an item in list\
           \n5 - Remove an item from list\
           \n6 - Add an item to list\
           \n7 - Print invalid groceries\
           \n8 - Remove duplicates from list\
           \n9 - Exit
           """)

    while True:
        user_choice = int(input("Choose an option (1-9): "))

        if user_choice == 1:
            print(groceries)
        elif user_choice == 2:
            print(len(groceries))
        elif user_choice == 3:
            print(search_in_list(groceries))
        elif user_choice == 4:
            print(count_in_list(groceries))
        elif user_choice == 5:
            groceries = remove_from_list(groceries)
        elif user_choice == 6:
            groceries.append(input("Enter an item to add to list: "))
        elif user_choice == 7:
            print_invalid_groceries(groceries)
        elif user_choice == 8:
            groceries = remove_duplicates(groceries)
        else:
            break  # User didn't choose 1-8 (assume 9)

        print()  # New line


def search_in_list(groceries_list):
    """
    Searches for a string (from user) in a given list
    :param groceries_list: The list to search through
    :type groceries_list: list
    :return: Whether element is in list or not
    :rtype: boolean
    """
    string = input("Enter an item to find: ")
    return string in groceries_list


def count_in_list(groceries_list):
    """
    Counts occurrences of a string (from user) in a given list
    :param groceries_list: The list to count through
    :type groceries_list: list
    :return: # of element in the list
    :rtype: int
    """
    string = input("Enter an item to count: ")
    return groceries_list.count(string)


def remove_from_list(groceries_list):
    """
    Removes an item from the list, if it's found
    :param groceries_list: The list to remove from
    :type groceries_list: list
    :return: The list after the item was removed
    :rtype: list
    """
    string = input("Enter an item to remove: ")
    if string not in groceries_list:
        print(string, "isn't in your groceries list!")
        return groceries_list
    # Valid element to remove:
    print(string, "removed from list")
    groceries_list.remove(string)
    return groceries_list


def print_invalid_groceries(groceries_list):
    """
    Prints a list of the elements that contain non-alphabetic
    chars or that are shorter than 2 characters
    :param groceries_list: The list to check
    :type groceries_list: list
    :return: None
    """
    invalid_items = [x for x in groceries_list if not x.isalpha() or len(x) < MAX_ITEM_LEN]
    print(invalid_items)


def remove_duplicates(groceries_list):
    """
    Removes duplicates of elements in a list
    :param groceries_list: The list to check
    :type groceries_list: list
    :return: The new list (with removed duplicates)
    :rtype: list
    """
    return list(set(groceries_list))


if __name__ == "__main__":
    main()
