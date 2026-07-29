# SIMPLE CALCULATOR IN PYTHON

def calculate():
    print("=" * 30)
    print("      SIMPLE CALCULATOR      ")
    print("=" * 30)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor Division (//)")
    print("6. Exponentiation (**)")
    print("7. Average")
    print("8. Modulus/Remainder (%)")
    print("=" * 30)

    # Get operation choice
    choice = input("Select an operation (1-8): ").strip()

    if choice not in [str(i) for i in range(1, 9)]:
        print("❌ Invalid selection! Please choose a number between 1 and 8.")
        return

    # Get numeric inputs safely
    try:
        a = float(input("Enter first number  --> "))
        b = float(input("Enter second number --> "))
    except ValueError:
        print("❌ Invalid input! Please enter numeric values only.")
        return

    # Perform calculations based on choice
    print("-" * 30)
    if choice == "1":
        print(f"Result: {a} + {b} = {a + b}")
    elif choice == "2":
        print(f"Result: {a} - {b} = {a - b}")
    elif choice == "3":
        print(f"Result: {a} * {b} = {a * b}")
    elif choice == "4":
        if b == 0:
            print("❌ Error: Division by zero is not allowed.")
        else:
            print(f"Result: {a} / {b} = {a / b}")
    elif choice == "5":
        if b == 0:
            print("❌ Error: Division by zero is not allowed.")
        else:
            print(f"Result: {a} // {b} = {a // b}")
    elif choice == "6":
        print(f"Result: {a} ** {b} = {a ** b}")
    elif choice == "7":
        print(f"Result: Average of {a} and {b} = {(a + b) / 2}")
    elif choice == "8":
        print(f"Result: {a} % {b} = {a % b}")


# Main program loop
if __name__ == "__main__":
    while True:
        calculate()
        print("-" * 30)
        again = input("Do you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break