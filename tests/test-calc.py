# Global variables
x = 9
y = 7

# Function to add two numbers
def add(x, y):
    return x + y


# Function to subtract two numbers
def subtract(x, y):
    return x - y


# Function to multiply two numbers
def multiply(x, y):
    return x * y


# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"


# Main program
def main():
    # Example numbers
    num1 = 10
    num2 = 5
    
    # Perform calculations with num1 and num2
    result_add = add(num1, num2)
    result_subtract = subtract(num1, num2)
    result_multiply = multiply(num1, num2)
    result_divide = divide(num1, num2)
    
    # Perform calculations with global variables x and y
    global_add = add(x, y)
    global_subtract = subtract(x, y)
    global_multiply = multiply(x, y)
    global_divide = divide(x, y)
    
    # Print results with num1 and num2
    print(f"Calculations with num1 = {num1} and num2 = {num2}:")
    print(f"{num1} + {num2} = {result_add}")
    print(f"{num1} - {num2} = {result_subtract}")
    print(f"{num1} * {num2} = {result_multiply}")
    print(f"{num1} / {num2} = {result_divide}")
    
    # Print results with global variables x and y
    print(f"\nCalculations with x = {x} and y = {y}:")
    print(f"{x} + {y} = {global_add}")
    print(f"{x} - {y} = {global_subtract}")
    print(f"{x} * {y} = {global_multiply}")
    print(f"{x} / {y} = {global_divide}")

# Run the main program
main()
