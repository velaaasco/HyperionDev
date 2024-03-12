# main.py

def calculate_sum(a, b):
   
    return a + b

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
