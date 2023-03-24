def copy_file_content(source, destination):
    """
    Copies contents of a file in source
    path to a file in destination path
    :param source: The path of the file to copy
    :type source: str
    :param destination: The path of the file to paste to
    :type destination: str
    :return: None
    """
    with open(source, 'r') as src_file:
        with open(destination, 'w') as dst_file:
            dst_file.write(src_file.read())


copy_file_content("copy.txt", "paste.txt")
