print("..................Welcome to calculator......................")
operation = input("Please ! let me know what you want to do +, -, *, /, % Please write it... ")
number1 = float(input("Enter the 1st number: "))
number2 = float(input("Eneter the 2nd nummbe: "))

if operation =="+":
    result = number1 + number2
    print(result)
elif operation == "-":
    result = number1 - number2
    print(result)
elif operation == "*":
    result = number1 * number2
    print(result)
elif operation == "%":
     if number2 == 0.0:
        print("You can not give zero to second value ")
        number2= float(input("Enter the 2nd number oncec again: "))

        while number2 ==  0: # loop at least number is greater than Zero 
            print("you cannot give zero value in second number.")
            number2 = float(input("Enter the second number again: "))
            
        result = number1 % number2
        print(result)
     else:
        result = number1 % number2
        print(result )
     print(result)
elif operation == "/":
    if number2 == 0.0:
        print("You can not give zero to second value ")
        number2= float(input("Enter the 2nd number oncec again: "))

        while number2 ==  0: # loop at least number is greater than Zero 
            print("you cannot give zero value in second number.")
            number2 = float(input("Enter the second number again: "))

        result = number1 / number2
        print(result)
    else:
        result = number1 / number2
        print(result )
    
    