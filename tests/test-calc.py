# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Main function to run the calculator
def main():
    print("Simple Calculator")

    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        # Check if choice is one of the options
        if choice in ('1', '2'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
        
        elif choice == '3':
            print("Exiting the program...")
            break
        
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
