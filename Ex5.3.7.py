SMALL_LENGTH, BIG_LENGTH = 1, 5


def chocolate_maker(small, big, x):
    return (small * SMALL_LENGTH + big * BIG_LENGTH) >= x


print(chocolate_maker(3, 2, 10))
