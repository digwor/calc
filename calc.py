def addition(z):
    print()
    print('1. a + b')
    while True:
        a = input('Введите a: ')
        b = input('Введите b: ')
        if a.isdigit() and b.isdigit():
            z = int(a) + int(b)
            print('Результат a + b =: ', z)
            input('Для продолжения нажмите Enter...')
            break
        else:
            input('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
            continue

def subtraction(z):
    print()
    print('2. a - b')
    while True:
        a = input('Введите a: ')
        b = input('Введите b: ')
        if a.isdigit() and b.isdigit():
            z = int(a) - int(b)
            print('Результат a - b =: ', z)
            input('Для продолжения нажмите Enter...')
            break
        else:
            input('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
            continue

def division(z):
    print()
    print('3. a / b')
    while True:
        a = input('Введите a: ')
        b = input('Введите b: ')
        if a.isdigit() and b.isdigit():
            z = float(a) / float(b)
            print('Результат a / b =: ', z)
            input('Для продолжения нажмите Enter...')
            break
        else:
            input('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
            continue

def multiplication(z):
    print()
    print('4. a * b')
    while True:
        a = input('Введите a: ')
        b = input('Введите b: ')
        if a.isdigit() and b.isdigit():
            z = int(a) * int(b)
            print('Результат a * b =: ', z)
            input('Для продолжения нажмите Enter...')
            break
        else:
            input('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
            continue

def fibonacci(z):
    print()
    print('5. Число Фибоначчи')
    while True:
        n = input('Введите число: ')
        if n.isdigit():
            t1 = 0
            t2 = 1
            for _ in range(0, int(n)):
                t1, t2 = t2, t1 + t2
                print(t1, end=' ')
            input('\nДля продолжения нажмите Enter...')
            break
        else:
            input('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
            continue

def  sqrt(z):
    print()
    print('6. √')
    while True:
        n = input('Введите число: ')
        if n.isdigit():
            z = int(n) ** (0.5)
            print('Результат √ =: ', z)
            input('Для продолжения нажмите Enter...')
            break
        else:
            input('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
            continue

def menu():
    print()
    print('Калькулятор')
    print('1. a + b')
    print('2. a - b')
    print('3. a / b')
    print('4. a * b')
    print('5. Число Фибоначчи')
    print('6. Квадратный корень')
    print('7. Выход')
    print('Выберите операцию: ', end='')

menu()
result = 0

while True:
    number = input()
    if  number.isdigit():
        while int(number) != 7:
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
            elif int(number) == 6:
                sqrt(number)
            menu()
            number = input()
        break
    else:
        print('Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором')
        input('Для продолжения нажмите Enter...')
        menu()


print('Good bye!')