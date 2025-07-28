

def calculator():
    print("Welcome to the Simple Calculator!")
    print("You can perform addition (+), subtraction (-), multiplication (*), or division (/).")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error: Cannot divide by zero.")
        else:
            print("Invalid operation selected.")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
calculator()
