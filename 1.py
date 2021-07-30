import math

a = float(input('pls enter number1: '))
op = input('pls enter operator: ')

if op == '+' or op == '-' or op == '*' or op == '/':
    
    b = float(input('pls enter number2: '))

    if op == '+':
        result = a+b

    elif op == '-':
        result = a-b

    elif op == '*':
        result = a*b

    elif op == '/':
        if b == 0:
            result = 'error,Cannot divide by zero'
        else:
            result = a/b
    print(result)

else:
    
    if op == 'radical':
        print('radical num1 is :', math.sqrt(a))

    elif op == 'sin':
        print('sin num1 is :', math.sin(math.degrees(a)))

    elif op == 'cos':
        print('cos num1 is :', math.cos(math.degrees(a)))

    elif op == 'tan':
        print('tan num1 is :', math.tan(math.degrees(a)))

    elif op == 'factorial':
        print('factorial num1 is :', math.factorial(a))