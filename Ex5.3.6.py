def filter_teens(a=13, b=13, c=13):
    return fix_age(a) + fix_age(b) + fix_age(c)


def fix_age(age):
    if 13 <= age <= 19 and not(age == 15 or age == 16):
        return 0  # Reset age (teen)
    return age  # Else, valid


print(filter_teens())
