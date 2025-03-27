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

    additionSum = num1 + num2

    print(f"The result is {additionSum}")

if method == 2:

    print("SUBTRACTION(-)")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    SubtSum = num1 - num2

    print(f"The result is {SubtSum}")
