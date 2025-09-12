# Simple Calculator Program

print("----- Simple Calculator -----")
print("Operations: +  -  *  /")

# Taking input from user
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Performing calculation
if op == "+":
    print("Result =", num1 + num2)
elif op == "-":
    print("Result =", num1 - num2)
elif op == "*":
    print("Result =", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operator!")

# Example Output:
# ----- Simple Calculator -----
# Operations: +  -  *  /
# Enter first number: 15
# Enter operator (+, -, *, /): *
# Enter second number: 3
# Result = 45.0
