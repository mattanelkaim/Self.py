import calendar

date = input("Enter a date: ")
day_of_week_number = calendar.weekday(int(date[-4:]), int(date[3:5]), int(date[:2]))
day_name = calendar.day_name[day_of_week_number]  # Get day name using built-in function
print(day_name)
