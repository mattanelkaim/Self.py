user_str = input("Please enter a string: ")
# Replace occurrences of first letter in str with 'e'
user_str = user_str[0] + user_str[1:].replace(user_str[0], 'e')
print(user_str)
