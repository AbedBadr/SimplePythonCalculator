# Simple python calculator

# Function adds 2 numbers together
def add(x, y):
	return x + y

# Function subtracts 2 numbers
def subtract(x, y):
	return x - y

# Function multiplies 2 numbers
def multiply(x, y):
	return x * y

# Function divides 2 numbers
def divide(x, y):
	return x / y

print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# User input
operation = input("Enter operation: ")

firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter second number: "))

if operation == "1":
	print("{} + {} = " .format(firstNumber, secondNumber), add(firstNumber, secondNumber))

elif operation == "2":
	print("{} - {} = " .format(firstNumber, secondNumber), subtract(firstNumber, secondNumber))

elif operation == "3":
	print("{} * {} = " .format(firstNumber, secondNumber), multiply(firstNumber, secondNumber))

elif operation == "4":
	print("{} / {} = " .format(firstNumber, secondNumber), divide(firstNumber, secondNumber))

else:
	print("Invalid input")