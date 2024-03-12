# main.py

# Function to calculate the sum of two numbers
def calculate_sum(a, b):
    # Add two numbers and return the result
    return a + b

# Main function to execute the program
def main():
    # Input two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Calculate the sum of the numbers
    result = calculate_sum(num1, num2)
    
    # Display the result
    print("The sum of", num1, "and", num2, "is:", result)

# Call the main function to start the program
if __name__ == "__main__":
    main()
