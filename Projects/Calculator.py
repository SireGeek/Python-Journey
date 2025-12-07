print("Well Helloooo, This is a simple calculator.")

while True:
    operation = input('What operation would you want to solve? (add, subtract, quit): ').lower()
    
    if operation == 'quit':
        print("Goodbye!")
        break
    
    if operation in ['add', '+']:
        try:
            a = int(input("Addition Selected! What is the first number?: "))
            b = int(input("Addition Selected! What is the second number?: "))
            print(f"Result: {a + b}")
        except ValueError:
            print('Please enter a valid number.')
    
    elif operation in ['subtract', '-']:
        try:
            a = int(input('Subtraction Selected! What is the first number?: '))
            b = int(input('Subtraction Selected! What is the second number?: '))
            print(f"Result: {a - b}")
        except ValueError:
            print('Please enter a valid number.')
    
    else:
        print("Invalid operation. Try again.")
