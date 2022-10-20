# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

try:
    def create_list(num):
        list = []
        for i in range(num):
            list.append(int(input('Введите число: ')))
        return list

    def summa_list(list):
        sum = 0
        for i in range(len(list)):
            if i % 2 != 0:
                sum += list[i]
        return sum

    def print_list():
        size = int(input('Введите размер списка (от 2): '))
        if size < 2:
            print('!! Размер списка не может быть меньше 2 !!')
            return
        list = create_list(size)
        print('Результат формирования списка:')
        print(list)
        print(f'Сумма чисел на нечётных позициях: {summa_list(list)}')

    print_list()
except: 
    print ('!! Введите целое число !!')