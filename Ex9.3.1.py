def my_mp3_playlist(file_path):
    """
    Extract songs data from a given file path, find:
    longest song name, total songs, most popular singer.
    Template of file:
    <song_name>;<singer>;<song_length>;\n
    :param file_path: The path to the file
    :type file_path: str
    :return: the longest song name, total songs, most popular singer
    :rtype: tuple
    """
    with open(file_path, 'r') as file:
        # List of lists: each list contains the elements of the song
        songs = [line.split(";")[:3] for line in file]

    singers = [song[1] for song in songs]

    # Find the longest song (last element), then get its name [0]
    longest_song = sorted(songs, key=lambda x: x[2])[-1][0]
    # Use lambda in sort to find most common element
    most_popular_singer = sorted(singers, key=lambda x: singers.count(x))[-1]
    total_songs = len(songs)

    return longest_song, total_songs, most_popular_singer


print(my_mp3_playlist(r"songs.txt"))
