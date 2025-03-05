#2359284 - Individual assignment 2
import random

# Constant for the student ID
STUDENT_ID = "2359284"

def generate_expression(n):
    """
    Generates a random mathematical expression with `n` operands.
    
    Parameters:
        n (int): Number of operands (between 3 and 5).
    
    Returns:
        str: The generated mathematical expression as a string.
        float: The evaluated result of the expression.
    """
    # Allowed operations
    operators = ['+', '-', '*', '/']
    
    # Generate random operands
    operands = [random.randint(0, 100) for _ in range(n)]
    
    # Generate random operators
    operations = [random.choice(operators) for _ in range(n - 1)]
    
    # Build the expression string
    expression = str(operands[0])
    for i in range(n - 1):
        expression += operations[i] + str(operands[i + 1])
    
    # Evaluate the expression
    try:
        result = eval(expression)  # Evaluating the generated expression
    except ZeroDivisionError:
        return generate_expression(n)  # Retry if division by zero occurs

    # Format the result to 3 decimal places if it's a float
    if isinstance(result, float):
        result = round(result, 3)
    
    return expression, result

def main():
    """
    Main function that asks for user input for each expression, 
    generates them, and writes them to a file.
    """
    expressions = []

    # Ask for the number of operands for each of the 4 expressions
    for _ in range(4):
        while True:
            try:
                n = int(input("Please input an integer between 3 and 5 inclued: "))  # Read input without displaying any message
                if 3 <= n <= 5:
                    break
            except ValueError:
                pass  # Ignore invalid input and ask again

        # Generate the expression with the given number of operands
        expressions.append(generate_expression(n))

    # Write results to "result.txt"
    with open("result.txt", "w") as file:
        file.write(STUDENT_ID + "\n")
        for expr, result in expressions:
            file.write(f"{expr}={result}\n")
    
    print("Program ended successfully!")
    print("Look at the output in the file result.txt in the same folder of the program.")

# Run the program
if __name__ == "__main__":
    main()
