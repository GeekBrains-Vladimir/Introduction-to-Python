# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
print("\033c")
A = int(input('Дружище, введи число любое, целое число: '))
my_list = []
while A > 0:
    B = int(A % 2)
    my_list.append(B)
    A = int(A / 2)
my_list.reverse()
print(*my_list, sep='')
