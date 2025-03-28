def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x, y):
    return  x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("Calculator by Neo")
print("Basic operations and supports decimals!")

while True:

    num1 = input("Enter first number: ")
    operator = input("Enter operation (+, -, x, /): ")
    num2 = input("Enter second number: ")

    try:
        num1 = float(num1)
        num2 = float(num2)

    except ValueError:
        print("Invalid input, try a real number.")

    if operator == "+":
        print(f"Result: {add(num1, num2)}")
    elif operator == "-": 
        print(f"Result: {subtract(num1, num2)}")
    elif operator == "x" or operator == "*":
        print(f"Result: {multiply(num1, num2)}")
    elif operator == "/":
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid operator, please retry!")
