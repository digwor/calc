def addition(z):
    print()
    print('1. a + b')
    while True:
        a = input('insert a: ')
        b = input('insert b: ')
        if a.isdigit() and b.isdigit():
            z = int(a) + int(b)
            print('Answer a + b =: ', z)
            input('Press Enter to continue...')
            break
        else:
            input('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
            continue

def subtraction(z):
    print()
    print('2. a - b')
    while True:
        a = input('insert a: ')
        b = input('insert b: ')
        if a.isdigit() and b.isdigit():
            z = int(a) - int(b)
            print('Answer a - b =: ', z)
            input('Press Enter to continue...')
            break
        else:
            input('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
            continue

def division(z):
    print()
    print('3. a / b')
    while True:
        a = input('insert a: ')
        b = input('insert b: ')
        if a.isdigit() and b.isdigit():
            z = float(a) / float(b)
            print('Answer a / b =: ', z)
            input('Press Enter to continue...')
            break
        else:
            input('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
            continue

def multiplication(z):
    print()
    print('4. a * b')
    while True:
        a = input('insert a: ')
        b = input('insert b: ')
        if a.isdigit() and b.isdigit():
            z = int(a) * int(b)
            print('Answer a * b =: ', z)
            input('Press Enter to continue...')
            break
        else:
            input('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
            continue

def fibonacci(z):
    print()
    print('5. Fibonacci number')
    while True:
        n = input('Insert number: ')
        if n.isdigit():
            t1 = 0
            t2 = 1
            for _ in range(0, int(n)):
                t1, t2 = t2, t1 + t2
                print(t1, end=' ')
            input('\nPress Enter to continue...')
            break
        else:
            input('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
            continue

def menu():
    print()
    print('Available option:')
    print('1. a + b')
    print('2. a - b')
    print('3. a / b')
    print('4. a * b')
    print('5. Fibonacci number')
    print('6. Exit')
    print('Enter option: ', end='')

menu()
result = 0

while True:
    number = input()
    if  number.isdigit():
        while int(number) != 6:
            if int(number) == 1:
                addition(result)
            elif int(number) == 2:
                subtraction(result)
            elif int(number) == 3:
                division(result)
            elif int(number) == 4:
                multiplication(result)
            elif int(number) == 5:
                fibonacci(result)
            menu()
            number = input()
        break
    else:
        print('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
        input('Press Enter to continue...')
        menu()


print('Good bye!')