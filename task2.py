print ("""Толстуха Надія. КМ-82
Варіант 23. Завдання 2.""")

import numpy as np
import random

# імпортуємо файл з валідацією
import work.validation

# імпортуємо файл з рекурсивними функціями
import work.recurcion

# початок циклу для виходу із програми
correct = False
while not correct:

    # Виклик функції для валідації вводу даних
    n = work.validation.get_number("Введіть кількість рядків:")

    # Створення рандомної матриці
    matrix = [[random.randrange(0,10) for y in range(n)] for x in range(n)]

    M = np.array(matrix)
    print(M)

    # Функція, що рекурсивно виводить рядки матриці, з елементами, що знаходяться над головною діагоняллю
    # def get_lines(matrix, current_index = 0):
    #     if matrix.size == 0:#Так як матриця знаходиться в модулі np, умова if matrix == [].... буде працювати лише зі звичайним списком, але не з ndarray.
    #         return None
    #     current_row = matrix[0]
    #     data = current_row[current_index +1:]
    #     print(data)
    #     return get_lines(matrix[1:], current_index+1)
    # print(get_lines(M))

    # Функція, що рекурсивно сумує елементи матриці, що знаходяться вище головної діагоналі.
    # Дана функція створена на основі ф-ції get_lines.
    # В цій ф-ції викликається ф-ція sum_list з файлу recurcion.py
    def sum_lines(matrix, current_index=0, current_sum=0):

        if matrix.size == 0:
            return current_sum
        current_row = matrix[0] #Визначаємо перший рядок матриці
        data = current_row[current_index + 1:]
        sum = work.recurcion.sum_list(list(data))
        return sum_lines(matrix[1:], current_index+1, current_sum+sum)#Через зрізи проходимо дал по всій матриці
    # Надання значення функції sum_lines()
    x = sum_lines(M)
    # Виклик функції sum_lines()
    print("Сума елементів матриці, що знаходяться вище головної діагоналі: ", x)

    # Функція, що рекурсивно виводить списки матриці з елементами вище побічної діагоналі
    # def get_other_lines(matrix, end_of_list = n-1):
    #     if end_of_list == 0:
    #         return None
    #     current_row = matrix[0]
    #     data = current_row[:end_of_list]
    #     print(data)
    #     return get_other_lines(matrix[1:], end_of_list-1)
    # print(get_other_lines(M))



    def mult_lines(matrix, end_of_list = n-1, current_mult = 1):
        if end_of_list == 0:
            return current_mult
        current_row = matrix[0]
        data = current_row[:end_of_list]
        mult = work.recurcion.mult_list(list(data), end_of_list)
        return mult_lines(matrix[1:], end_of_list-1, current_mult*mult)
    y =mult_lines(M)
    print("Добуток елементів матриці, що знаходяться вище побічної діагоналі: ", y)
    choice = input("Якщо хочете завершити програму - натисніть 1, а якщо повторити - будь-що.\n")
    if choice == "1":
        correct = True
    else:
        correct = False


'''
Примітка:
Коли пишете рекурсивну ф-цію спочатку пишіть саму ф-цію,
а потім вже думайте над умовою зупинки
'''
