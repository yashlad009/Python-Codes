try : 
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    print("what kind of operations do you want to perform \n + for addition \n - for substraction \n *for multiplication \n / for division")

    o = input("Enter operation:")

    match o :
        case '+':
            print(f"the result of {a} {o} {b} is {a + b}")
        case '-':
            print(f"the result of {a} {o} {b} is {a - b}")
        case '*':
            print(f"the result of {a} {o} {b} is {a * b}")
        case '/':
             
            print(f"the result of {a} {o} {b} is {a / b}")
        case _:  # Default case for invalid operations
            print("Invalid operation. Please enter +, -, *, or /")

except :
    print("Enter a valid Input")