def distance(num1, num2, num3):
    return abs(num1 - num2) == 1 and abs(num2 - num3) > 1 and abs(num3 - num1) > 1\
        or abs(num1 - num3) == 1 and abs(num3 - num2) > 1 and abs(num2 - num1) > 1


print(distance(1, 2, 10))
