# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06
print("\033c")
print('Программа, принимает список из n чисел последовательности (1 + 1/n)^n, выводит его на экран, а так же сумму элементов списка')
print('')
N = int(input('Дружище, введи целое число: '))
Reload = []
Sum = 0
for i in range(1, N+1):
    Funk = round((1+1/i)**i, 2)
    Sum += Funk
    Reload.append(Funk)
print(f'Последовательность: {Reload}')
print(f'Сумма всех значений равна: {Sum}')
