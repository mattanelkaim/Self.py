def func(num1, num2):
    """
    Calculates the sum of num1 and 2 * num2
    :param num1: The first number in calculation
    :type num1: int
    :param num2: The second number in calculation
    :type num2: int
    :return: The sum of num1 and 2 * num2
    :rtype: int
    """
    return num1 + 2 * num2


def main():
    print(func(2, 4))


if __name__ == '__main__':
    main()
