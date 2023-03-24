user_str = input("Please enter a string: ")
middle = len(user_str) // 2
user_str = user_str[:middle].lower() + user_str[middle:].upper()
print(user_str)
