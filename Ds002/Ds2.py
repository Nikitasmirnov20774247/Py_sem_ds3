# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


try:
    def create_list(num):
        list = []
        for i in range(num):
            list.append(int(input('Введите число: ')))
        return list

    def mult_num(list, size):
        list2 = []
        count = 0
        while count < len(list)/2:
            size -= 1
            mult = list[count] * list[size]
            list2.append(mult)
            count += 1
        return list2

    def print_list():
        size = int(input('Введите размер списка (от 2): '))
        if size < 2:
            print('!! Размер списка не может быть меньше 2 !!')
            return
        list = create_list(size)
        list2 = mult_num(list, size)
        print('Результат формирования списка:')
        print(list)
        print(f'Произведение пар чисел = {list2}')

    print_list()
except:
    print ('!! Введите целое число !!')