degrees = input("Insert the temperature you would like to convert: ").upper()
value = float(degrees[:-1])

if degrees[-1] == "C":  # In Celsius
    # Change to Fahrenheit
    degrees = str(value * 1.8 + 32) + "F"
else:  # In Fahrenheit
    # Change to Celsius
    degrees = str((value - 32) * 5 / 9) + "C"

print(degrees)
