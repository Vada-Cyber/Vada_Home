while True: 
     
    try: calculating = input('would you like to make a calculation? (y/n) ') 


    if calculating in ('y', 'yes'):
        try:
            numberOne = float(input('Enter your first number. '))
            operation = input('Enter your operator. ')
            if operation not in ('+', '-', '*', 'x', '/'):
                print('That is not an operator.')
                continue
            numberTwo = float(input('Enter your second number. '))
        except ValueError as e:
            print(e)
            continue

        if operation == '+':
            print(float(numberOne) + float(numberTwo))
        if operation == '-':
            print(float(numberOne) - float(numberTwo))
        if operation in ('*', 'x'):
            print(float(numberOne) * float(numberTwo))
        try:
            if operation == '/':
                print(float(numberOne) / float(numberTwo))
        except ZeroDivisionError:
            print('Error: Division by 0')
            continue

         elif calculating in ('n', 'no'):
        print('Okay')
        break

        if calculating not in ('y', 'n', 'yes', 'no'):
        print('It is one or the other')
        continue

    except Exception as e:
        print(e)