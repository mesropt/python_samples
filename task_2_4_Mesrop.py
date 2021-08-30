"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Массив в этом задании строить не нужно!
Нужно решить без него!
Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75
Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def recur_method(i, numb, n_count, common_sum):
    if i == n_count:
        print(f'Количество элементов - {n_count}, их сумма - {common_sum}')
    elif i < n_count:
        return recur_method(i + 1, numb / 2 * -1, n_count, common_sum+numb)

try:
    N_COUNT = int(input('Введите количество элементов:'))
    recur_method(0, 1, N_COUNT, 0)
except ValueError:
    print('Вы вместо числа ввели строку. Исправьтесь')