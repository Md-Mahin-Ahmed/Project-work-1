def main():
    print("Welcome to the Arithmetic Calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = int(input())

    result = 0.0

    if choice == 1:
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == 2:
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == 3:
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid choice. Please select a valid operation.")
if __name__ == "__main__":
    main()