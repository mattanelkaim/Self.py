def main():
    path = input("Enter the file path: ")
    operation = input("Enter the operation (last/rev/sort): ")

    with open(path, 'r') as file:
        content = file.read()

    if operation == "sort":
        words_list = []
        for word in content.split():
            if word not in words_list:
                words_list.append(word)
        words_list.sort()
        print(words_list)
    elif operation == "rev":
        for line in content.splitlines():
            print(line[::-1])
    elif operation == "last":
        number = int(input("Enter a number: "))
        list_of_last_lines = content.splitlines()[-number:]
        for line in list_of_last_lines:
            print(line)


if __name__ == '__main__':
    main()
