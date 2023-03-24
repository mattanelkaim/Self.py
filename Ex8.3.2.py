CURRENT_YEAR = 2020  # IMPORTANT! Feedback system only supports year 2020!


def main():
    person = {"first_name": "Mariah", "last_name": "Carey",
              "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}

    user_choice = int(input("Enter your choice: "))

    # Could have used match...case
    if user_choice == 1:
        print(person["last_name"])
    elif user_choice == 2:
        print(person["birth_date"][3:5])
    elif user_choice == 3:
        print(len(person["hobbies"]))
    elif user_choice == 4:
        print(person["hobbies"][-1])
    elif user_choice == 5:
        person["hobbies"].append("Cooking")
    elif user_choice == 6:
        date_parts = person["birth_date"].split(".")
        person["birth_date"] = (int(date_parts[0]),  # Day
                                int(date_parts[1]),  # Month
                                int(date_parts[2]))  # Year
        print(person["birth_date"])
    elif user_choice == 7:
        person["age"] = CURRENT_YEAR - int(person["birth_date"].split(".")[2])
        print(person["age"])


if __name__ == '__main__':
    main()
