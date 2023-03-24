def are_files_equal(file1, file2):
    """
    Compares the contents of 2 files
    :param file1: Path to first file
    :type file1: str
    :param file2: Path to second file
    :type file2: str
    :return: Whether file's contents are identical or not
    :rtype: boolean
    """
    with open(file1, 'r') as first_file:
        file1_contents = first_file.readline()
    with open(file2, 'r') as second_file:
        file2_contents = second_file.readline()
    return file1_contents == file2_contents
