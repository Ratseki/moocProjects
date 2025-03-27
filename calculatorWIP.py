print("*** CALCULATOR ****")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

method = int(input("Please select a method: "))

if method == 1:

    print("ADDITION(+)")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    sum = num1 + num2

    print(f"The result is {sum}")

if method == 2:

    print("SUBTRACTION(-)")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    sum = num1 - num2

    print(f"The result is {sum}")

if method == 3:

    print("MULTIPLICATION(*)")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    sum = num1 * num2

    print(f"The result is {sum}")

if method == 4:

    print("DIVISION(/)")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    sum = num1 / num2

    print(f"The result is {sum}")
