LINES_TO_JUMP = 3


def my_mp4_playlist(file_path, new_song):
    """
    Replaces name of third song in a given file with the new given name
    Template of file:
    <song_name>;<singer>;<song_length>;\n
    :param file_path: The path to the file to change
    :type file_path: str
    :param new_song: The new name of the third song
    :type new_song: str
    :return: None
    """
    with open(file_path, 'r') as file:
        songs = [line.split(";")[:3] for line in file]

    # If there are less than 3 lines
    while len(songs) < LINES_TO_JUMP:
        songs.append([""])
    songs[LINES_TO_JUMP - 1][0] = new_song  # Replace song name

    # Re-assemble file content
    new_content = ""
    for song in songs:
        new_content += ";".join(song)
        if song != [""]:  # If not a blank line
            new_content += ";"  # Add a closing ';'
        new_content += "\n"

    # Write new content
    with open(file_path, 'w') as file:
        file.write(new_content)
    print(new_content)


my_mp4_playlist("songs.txt", "Hello")
