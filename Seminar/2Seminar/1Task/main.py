# Напишите программу, которая, принимает на вход число N и выдаёт последовательность из N членов.
# * Пример *
# - Для N=5:
# 1, -3, 9, -27, 81
print("\033c")
print('Программа, которая, принимает на вход число N и выдаёт последовательность из N членов.')
print('')
number = int(input('Введите целое число: '))
for degree in range(number):
    print((-3)**degree)
