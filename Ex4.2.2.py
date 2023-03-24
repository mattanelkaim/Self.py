word = input("Enter a word: ").replace(" ", "").lower()  # Remove spaces & change to lowercase

if word == word[::-1]:  # If word == reversed word
    print("OK")
else:
    print("NOT")
