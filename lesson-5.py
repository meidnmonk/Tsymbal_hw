# ----------------------- 1 -----------------------
print('Task 1')
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Input new string or empty string to done: ')
        if not line:
            break
        print(line, file=f)
print(
)
# ----------------------- 2 -----------------------
print('Task 2')
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text_2.txt', 'r', encoding='utf-8') as f_obj:
    useful = [f'{line}. {count.strip()} - {len(count.split())} words'
              for line, count in enumerate(f_obj, 1)]
    print(*useful, f'Total line - {len(useful)}.', sep='\n')
print(

)
# ----------------------- 3 -----------------------
print('Task 3')
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Employees with salary less than 20k: {[e[0] for e in employees_dict.items() if el[1] < 20000]}')
print(
)
# ----------------------- 3.1 -----------------------
print('Task 3.1')

def task_3():
    wages = {}
    try:
        with open('task_3.txt', 'r', encoding='utf-8') as file:
            for line in file:
                wages[line.split()[0]] = float(line.split()[1])
        print('Get less than 20k:')
        for name, wage in wages.items():
            if wage < 20000:
                print(name)
        print(f'Average salary equals {sum(wages.values()) / len(wages)}')
    except IOError:
        print('No salary. Sorry')
    except:
        print('Something went wrong')

task_3()
print(
)
# ----------------------- 4 -----------------------
print('Task 4')
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_44.txt', 'w', encoding='utf-8') as new_file:
    with open('text_4.txt', encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])

print(
)

# ----------------------- 4.1 -----------------------
print('Task 4.1')

from googletrans import Translator

with open('text_4_translate.txt', 'w', encoding='utf-8') as f:
    with open('text_4.txt', 'r', encoding='utf-8') as f1:
        text = f1.read()
    try:
        f.write(Translator().translate(text, dest='ru').text)
    except AttributeError:
        print('Keep trying')
print(
)
# ----------------------- 5 -----------------------
print('Task 5')
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('text.txt', 'w', encoding='utf-8') as my_file:
    my_list = [randint(1, 100) for _ in range(100)]
    my_file.write(' '.join(map(str, my_list)))

print(f'Sum of elements equals {sum(my_list)}')
print(
)

# ----------------------- 5.1 -----------------------
print('Task 5.1')

from random import randint

with open('task_5_file.txt', mode='w+', encoding='utf-8') as the_file:
    the_file.write(' '.join([str(randint(1, 1000)) for _ in range(100000)]))
    the_file.seek(0)
    print(sum(map(int, the_file.readline().split())))

print(
)
# ----------------------- 6 -----------------------
print('Task 6')
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

my_dict = {}
with open('text_6.txt', encoding='utf-8') as fobj:
    for line in fobj:
        name, stats = line.split(':')
        name_sum = sum(map(nt, ''.join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        my_dict[name] = name_sum
print(f'{my_dict}')
print(
)

# ----------------------- 6.1 -----------------------
print('Task 6.1')

with open('text_6.txt', 'r', encoding='utf-8') as text_file:
    a = text_file.readlines()
    for s in a:
        new_str = ''.join((i if i in '1234567890' else ' ') for i in s)
        new_2 = [int(i) for i in new_str.split()]
        print(f'{s.split()[0]} {sum(new_2)}')

print(
)

# ----------------------- 6.2 -----------------------
print('Task 6.2')

result = {}
with open('text_6.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        lesson_timing = []
        lessons = ([el for el in line.split(' ')])
        for el in lessons:
            lesson_timing.append(''.join(i for i in list(el) if i.isdigit()))
        result[line.split(':')[0]] = sum([int(i) for i in lesson_timing if i.isdigit()])

print(result)
print(
)

# ----------------------- 6.3 -----------------------
print('Task 6.3')

with open('text_6.txt', 'r', encoding='utf-8') as file:
    print({string.split(':')[0]: sum([int(s[:s.index('(')]) for s in string.split() if '(' in s]) for string in line})

print(
)
# ----------------------- 7 -----------------------
print('Task 7')
# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

with open('my_ex7.json', 'w', encoding='utf-8') as write_f:
    with open('text_7.txt', encoding='utf-8') as f_obj:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
        result = [profit, {'average profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len(int(i) for i in profit.values() if int(i) > 0))}]
    json.dump(result, write_f, ensure_ascii=False, indent=4)
