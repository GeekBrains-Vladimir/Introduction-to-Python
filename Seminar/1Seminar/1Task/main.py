# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#
# *Примеры:*
#
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if b == a**2: # or a == b**2
    print(f'Второе число {b} является квадратом первого числа {a}')
elif a == b**2:
    print(f'Первое число {a} является квадратом второго числа {b}')
else:
    print('Числа не являются квадратом друг друга')
