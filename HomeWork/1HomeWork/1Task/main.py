# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет
print("\033c")
print('Программа, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным')
print('')
a = int(input('Дружок, введи число от 1 до 7 включительно: '))
while a < 1 or a > 7:
    print('')
    a = int(input('Дружок, НЕ ТУПИ, введи число от 1 до 7 включительно: '))
if a > 0 and a < 6:
    print('')
    print('Работаем в поте лица - будни')
else:
    print('')
    print('Гуляй, рванина - ВЫХОДНОЙ!')
