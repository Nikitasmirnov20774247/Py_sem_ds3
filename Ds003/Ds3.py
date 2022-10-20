# Задача 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def create_list(num):
        list = []
        for i in range(num):
            list.append(float(input('Введите число: ')))
        return list

def result_num(list):
    max = 0
    for i in list:
        if i%1 != 0:
            if (i - int(i)) >= max:
                max = i - int(i)
    min = max
    for i in list:
        if i%1 != 0:
            if (i - int(i)) <= min:
                min = i - int(i)
    r = max - min
    result = round(r, 2)
    return result

def print_list():
    size = int(input('Введите размер списка (от 2): '))
    if size < 2:
        print('!! Размер списка не может быть меньше 2 !!')
        return
    list = create_list(size)
    result = result_num(list)
    print('Результат формирования списка:')
    print(list)
    print(f'Разница между max и min значением дробной части элементов = {result}')

print_list()