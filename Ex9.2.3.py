def who_is_missing(file_name):
    """
    Finds the missing number from a non-ordered series
    of numbers, found in the file whose path is specified.
    Also writes the missing number into a new file.
    :param file_name: The path of the file containing the numbers
    :type file_name: str
    :return: The missing number
    :rtype: int
    """
    # Open source file
    with open(file_name, 'r') as file:
        nums_set = file.read().split(",")  # List of sorted nums (strings)

    nums_set = set(map(int, nums_set))  # Map to ints set
    max_num = len(nums_set) + 2  # Include itself and next
    for num in range(1, max_num):
        if num not in nums_set:
            # Write to found file
            with open(r"found.txt", 'w') as dst_file:
                dst_file.write(str(num))
            return num


print(who_is_missing(r"findMe.txt"))
