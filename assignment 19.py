x = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
y = float(input("Enter second number: "))

if operator == '+':
    print(f"Result: {x} + {y} = {x + y}")
elif operator == '-':
    print(f"Result: {x} - {y} = {x - y}")
elif operator == '*':
    print(f"Result: {x} * {y} = {x * y}")
elif operator == '/':
    if num2 != 0:
        print(f"Result: {x} / {y} = {x / y}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator! Please use +, -, *, or /.")   
