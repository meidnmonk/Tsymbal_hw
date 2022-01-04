# ------------------------------- 1 -------------------------------
print('Task 1')
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [(-1 + 0j), 1, 2.2, True, None, 'String', [3, 4], (5, 6, 6.5), {7: 'seven', 8: 'eight'}, {9, 10},
           frozenset(), range(11), b'twelve', bytearray(b'thirteen'), zip(*[(14, 15), (16, 17), ('a', 'b')]),
           TypeError]
for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")
print(
)
# ------------------------------- 2 -------------------------------
print('Task 2')
# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = list(input('Enter numbers without space: '))
for i in range(1, len(my_list), 2):
    my_list[i -1], my_list[i] = my_list[i], my_list[i-1]

# ------------------------------- 3 -------------------------------
print('Task 3')
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('Insert month number: '))
month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
              8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']

if month in month_dict:
    print(f'{month} month of a year is {month_dict[month]}')
    print(f'{month} month of a year is {month_list[month - 1]}')
else:
    print('Wrong month number')
print(
)
# ------------------------------- 4 -------------------------------
print('Task 4')
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

string = input('Enter text: ').split()
for n, i in enumerate(string, 1):
    print(f'{n}) {i:.10}')

print(
)
# ------------------------------- 5 -------------------------------
print('Task 5')
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [4, 3, 3, 2, 1]

while True:
    print(f'Current rating: {my_list}')
    number = input('Enter rating number or 111 to finish: ')
    if number.lstrip('-').isdigit() and number != '111':
        number = int(number)
        if my_list.count(number):
            my_list.insert(my_list.index(number) + my_list.count(number), float(number))
        else:
            param = 0
            n_param = 0
            for n, i in enumerate(my_list):
                if number > i:
                    if param <i:
                        param = i
                else:
                    n_param = i + 1
            my_list.insert(n_param, number)
    elif not number.isdigit():
        print('Enter number please')
    else:
        break
print(
)
# ------------------------------- 6 -------------------------------
print('Task 6')
# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
num = 0
while True:
    if input("Для выхода нажмите 'Q', для продолжения 'Enter': ").upper() == 'Q':
        break
    num += 1
    for f in features:
        pro = input(f'Введите значения свойства "{f}": ')
        features[f] = pro
    goods.append((num, features))
    print(goods)