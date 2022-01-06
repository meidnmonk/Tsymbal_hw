# --------------------------- 1 ---------------------------
print('Task 1')
#Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль

def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
       div_num = s_1 / s_2
    except ValueError:
        return 'Value Error'
    except ZeroDivisionerror:
        return 'Division by zero is forbidden'
    return round(div_num, 4)

print(div(input('Enter 1st number: '), input('Enter 2nd number: ')))
print(
)
# --------------------------- 2 ---------------------------
print('Task 2')
#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой

def personal_info(**kwargs):
    return ' '.join(kwargs.values())

print(personal_info(name=input('Enter name: '), surname=input('Enter surname: '),
                    birthday=input('Enter birthday date: '), city=input('Enter city: '),
                    email=input('Enter email: '), phone_number=input('Enter phone number: ')))
print(
)
# --------------------------- 3 ---------------------------
print('Task 3')
#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'Enter only numbers'

print(my_func(num_1=int(input('Enter 1st number: ')), num_2=int(input('Enter 2nd number: ')),
              num_3=int(input('Enter 3rd number: '))))

print(
)
# --------------------------- 3.1 ---------------------------
print('Task 3.1')
def my_func(num_1, num_2, num_3):
    return sum(sorted([num_1, num_2, num_3])[1:])

print(my_func(num_1=int(input('Enter 1st number: ')), num_2=int(input('Enter 2nd number: ')),
              num_3=int(input('Enter 3rd number: '))))

print(
)
# --------------------------- 4 ---------------------------
print('Task 4')
#Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).

def my_func(x, y):
    try:
        res = x ** y
    except TypeError:
        return 'Enter float number and negative power'
    return res

print(my_func(x=float(input('Enter float number: ')), y=int(input('Enter negative power: '))))

print(
)
# --------------------------- 4.1 ---------------------------
print('Task 4.1')
#Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень

def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Enter float number and negative power'
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return f'Результат возведения {x} в степень {y} равен {round(result, 6)}'
    except ValueError:
        return 'Программа работает только с числами'

number_1 = input('Enter float number x= ')
number_2 = input('Enter negative power y= ')

print(my_func(number_1, number_2))
print(
)
# --------------------------- 5 ---------------------------
print('Task 5')
#Программа запрашивает у пользователя строку чисел, разделенных пробелом.
#При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_num():
    s = 0
    while True:
        in_list = input('Enter numbers, press "q" to exit: ').split()
        for num in in_list:
            if num.lower() == "q":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print('To exit the programme enter "q": ')
        print(f'Sum of numbers equals {s}')

print(sum_num())

print(
)
# --------------------------- 6 ---------------------------
print('Task 6')
#Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func():
    for word in input('Enter words with lower latin script with a space:\n').split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f'{word} - only small letters')

int_func()
print(
)
# --------------------------- 6.1 ---------------------------
print('Task 6.1')
int_func = lambda word: word.title() if word.islower() and ascii(word)[1:-1].isalpha() else ''
print(' _ '.join(map(int_func, input('Enter phrase: ').split())))