# Factorial Program in Python

# Taking input from user
n = int(input("Enter a number: "))

fact = 1
for i in range(1, n + 1):
    fact *= i   # fact = fact * i

print("Factorial:", fact)

# ------------------------------
# Example Output:
# Enter a number: 5
# Factorial: 120
