# Function to add two numbers
x=9
y=7
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
    
    # Perform calculations
    result_add = add(num1, num2)
    result_subtract = subtract(num1, num2)
    result_multiply = multiply(num1, num2)
    result_divide = divide(num1, num2)
    
    # Print results
    print(f"{num1} + {num2} = {result_add}")
    print(f"{num1} - {num2} = {result_subtract}")
    print(f"{num1} * {num2} = {result_multiply}")
    print(f"{num1} / {num2} = {result_divide}")

# Run the main program
main()
