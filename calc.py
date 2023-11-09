while True:
    print('1 Addition')
    print('2 Subtraction')
    print('3 Multiplication')
    print('4 Division')
    print('Enter q to Exit')

    choice = input('Choose an operation : ')

    if choice == 'q':
        break

    num1 = int(input('Enter Number 1 : '))
    num2 = int(input('Enter Number 2 : '))

    if choice == '1':
        print(num1, '+', num2, '=', (num1+num2))
    elif choice == '2':
        print(num1, '-', num2, '=', (num1-num2))
    elif choice == '3':
        print(num1, '*', num2, '=', (num1*num2))
    elif choice == '4':
        if num2 == 0:
            print('Divide by 0 Error')
        else:
            print(num1, '/', num2, '=', (num1/num2))
    else:
        print('Invalid Choice')

    print()