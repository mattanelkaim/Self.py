def last_early(my_str):
    # Is last char appears more than once
    my_str = my_str.lower()
    return my_str.count(my_str[-1]) != 1


print(last_early("Hii"))
