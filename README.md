# Python Calculator
Description:
This is a simple **Python-based calculator** that performs basic arithmetic operations.  
It takes two numbers as input from the user and performs the chosen operation (`+`, `-`, `*`, `/`, `%`).  
The program includes **error handling** to prevent division or modulus by zero.

Features:
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`) with zero check
- Modulus (`%`) with zero check
- User-friendly input prompts
- Validates input for second number when dividing or finding modulus
  
How It Works:
1. The program asks the user to select an operation (`+`, `-`, `*`, `/`, `%`).
2. The user enters the first and second numbers.
3. The program performs the calculation.
4. If the user tries to divide or take modulus by zero, it asks for a valid number again.
5. The result is displayed.

Code Example:
```python
print("..................Welcome to calculator......................")
operation = input("Please ! let me know what you want to do +, -, *, /, % Please write it... ")
number1 = float(input("Enter the 1st number: "))
number2 = float(input("Enter the 2nd number: "))

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "%":
    if number2 == 0.0:
        print("You cannot give zero to second value.")
    else:
        print(number1 % number2)
elif operation == "/":
    if number2 == 0.0:
        print("You cannot give zero to second value.")
    else:
        print(number1 / number2)
