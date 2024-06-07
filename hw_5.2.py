'hw_5.2'
while True:
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    math_operation = input('Enter math operation: ')
    success = True

    if math_operation == '/' and int(num2) == 0:
        print('Division by zero')
        success = False
    else:
        if math_operation == '+':
            result = int(num1) + int(num2)
        elif math_operation == '-':
            result = int(num1) - int(num2)
        elif math_operation == '*':
            result = int(num1) * int(num2)
        elif math_operation == '/':
            result = float(num1) / float(num2)
        else:
            print('Invalid operation')
            success = False
    if success:
        print(f'Result: {result}')

    request_to_continue = input('Enter "yes" (or just "y") if you want to continue >> ').lower()
    if request_to_continue not in ['yes', 'y']:
        print('Program terminated')
        break