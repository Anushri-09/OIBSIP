print("=" * 50)
print("           BMI CALCULATOR")
print("=" * 50)

while True:
    try:
        weight = float(input("\nEnter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than zero.")
            continue

        bmi = weight / (height ** 2)

        print("\n" + "=" * 50)
        print("YOUR BMI REPORT")
        print("=" * 50)
        print(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category : Underweight")
        elif bmi < 25:
            print("Category : Normal Weight")
        elif bmi < 30:
            print("Category : Overweight")
        else:
            print("Category : Obese")

        print("=" * 50)

    except ValueError:
        print("Please enter valid numbers.")

    choice = input("\nDo you want to calculate again? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using BMI Calculator!")
        break
