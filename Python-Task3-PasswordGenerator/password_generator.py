import random
import string

print("=" * 50)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 50)

while True:
    try:
        # Password Length
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        print("\nSelect character types:")
        print("1. Uppercase Letters")
        print("2. Lowercase Letters")
        print("3. Numbers")
        print("4. Symbols")

        upper = input("Include Uppercase? (yes/no): ").lower() == "yes"
        lower = input("Include Lowercase? (yes/no): ").lower() == "yes"
        numbers = input("Include Numbers? (yes/no): ").lower() == "yes"
        symbols = input("Include Symbols? (yes/no): ").lower() == "yes"

        character_set = ""

        if upper:
            character_set += string.ascii_uppercase

        if lower:
            character_set += string.ascii_lowercase

        if numbers:
            character_set += string.digits

        if symbols:
            character_set += string.punctuation

        selected = sum([upper, lower, numbers, symbols])

        if selected < 2:
            print("\nPlease select at least TWO character types.")
            continue

        password = ""

        for i in range(length):
            password += random.choice(character_set)

        print("\nGenerated Password:")
        print(password)

        again = input("\nGenerate another password? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using Password Generator!")
            break

    except ValueError:
        print("\nPlease enter a valid number.")
