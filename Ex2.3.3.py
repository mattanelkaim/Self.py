NUM_OF_PIGS = 3

number = input("Enter three digits (each digit for one pig): ")

# Section 1
total_bricks = sum(map(int, number))  # First turn to ints, then calculate sum
print(total_bricks)

# Section 2
print(total_bricks // NUM_OF_PIGS)

# Section 3
bricks_remainder = total_bricks % NUM_OF_PIGS
print(bricks_remainder)

# Section 4
print(bricks_remainder == 0)
